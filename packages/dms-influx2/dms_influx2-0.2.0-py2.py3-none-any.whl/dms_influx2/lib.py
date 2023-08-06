import logging
from collections import OrderedDict
from typing import List

from ciso8601 import parse_datetime
from influxdb_client import InfluxDBClient, Point, ChecksService, HTTPNotificationEndpoint, \
    NotificationEndpointsService
from datetime import datetime, timedelta
from influxdb_client.client.flux_table import FluxTable
from influxdb_client.client.write_api import SYNCHRONOUS, WriteOptions

from dms_influx2.authorizations import Authorizations
from dms_influx2.buckets import Buckets
from dms_influx2.checks import ChecksApi
from dms_influx2.decorators import runtime
from dms_influx2.delete import Delete
from dms_influx2.notifications import NotificationEndpointApi, NotificationRuleApi
from dms_influx2.organisations import Organizations
from dms_influx2.query import get_flux_query
from dms_influx2.tasks import Tasks
import pytz

from dms_influx2.utils import localize_dt

logger = logging.getLogger(__name__)


class DmsInflux2(InfluxDBClient):
    def __init__(self,
                 url=None,
                 token=None,
                 org=None,
                 enable_gzip=True,
                 timezone_offset: int = None,
                 timeout=20_000,
                 timezone='Europe/Ljubljana'):
        self.query_str = None
        self.predicates = None

        self.time_offset = timezone_offset
        self.time_shift = f'{timezone_offset}h' if timezone_offset is not None else None

        self.timezone = timezone

        super().__init__(url=url, token=token, org=org, enable_gzip=enable_gzip, timeout=timeout)

    def buckets_api(self) -> Buckets:
        return Buckets(self)

    def organizations_api(self) -> Organizations:
        return Organizations(self)

    def delete_api(self) -> Delete:
        return Delete(self)

    def authorizations_api(self) -> Authorizations:
        return Authorizations(self)

    def checks_api(self):
        return ChecksApi(self)

    def notification_endpoint_api(self):
        return NotificationEndpointApi(self)

    def notification_rule_api(self):
        return NotificationRuleApi(self)

    def tasks_api(self) -> Tasks:
        return Tasks(self)

    def _list_tag_values(self, bucket, measurement, tag, **kwargs):
        query = f'import "influxdata/influxdb/schema"\n\nschema.measurementTagValues(' \
                f'bucket: "{bucket}",' \
                f'measurement: "{measurement}",' \
                f'tag: "{tag}")'
        self.query_str = query
        tables = self.query_api().query(query)
        data = []
        for table in tables:
            for record in table.records:
                data.append(record.get_value())
        return data

    def _list_distinct_tags(self, bucket, measurement, tag='description', time_range=None):

        if time_range is None:
            time_range = 'all'

        tables = self._get_tables(bucket=bucket,
                                  measurement=measurement,
                                  time_range=time_range,
                                  last=True,
                                  group_columns=[tag],
                                  distinct=True)
        return self._convert_tables_key(tables, key=tag)

    def _perform_query(self, query, params=None):
        query_api = self.query_api()
        self.query_str = query
        # print(query)
        return query_api.query(query, params=params)

    def _convert_tables_key(self, tables, key='description'):
        data = []
        for table in tables:
            for record in table.records:
                value = record.values.get(key)
                if value:
                    data.append(value)
        return data

    @runtime
    def _extract_tables(self, tables: List['FluxTable'], values_name='values') -> list:

        data = []
        for table in tables:
            labels = [i.label for i in table.columns]
            try:
                get_columns = list(filter(lambda x: (x[0] != '_' and x not in ['table', 'result']), labels))
            except Exception as e:
                # TODO try to resolve this error
                for record in table.records:
                    logger.error(record)
                continue
            _data = {}
            _values = []
            for record in table.records:
                if not _data:
                    for col in get_columns:
                        _data[col] = record.values.get(col, None)
                ts = str(record.get_time()).split('+')[0]
                _values.append((ts, record.get_value()))
            data.append({**_data, values_name: _values})
        return data

    @runtime
    def _get_tables(self, **kwargs) -> List['FluxTable']:
        """Return tables based on flux query"""
        query = get_flux_query(**kwargs, time_shift=self.time_shift, time_offset=self.time_offset)
        return self._perform_query(query=query)

    def list_measurements(self, bucket) -> list:
        """Return list of measurements inside a bucket"""

        query = f'import "influxdata/influxdb/schema"\n\nschema.measurements(bucket: "{bucket}")'
        self.query_str = query
        tables = self.query_api().query(query)
        data = []
        for table in tables:
            for record in table.records:
                data.append(record.get_value())
        return data

    def list_device_ids(self, bucket, measurement=None) -> list:
        """Return list of distinct device_ids (tag=device_id)"""

        return self._list_distinct_tags(bucket=bucket, measurement=measurement, tag='device_id')

    def list_descriptions(self, bucket, measurement=None, time_range=None) -> list:
        """Return list of distinct descriptions"""

        if time_range is None:
            time_range = '100y'

        predicate = f'r._measurement == "{measurement}"' if measurement else 'true'

        query = f'''import "influxdata/influxdb/schema"\n\n
        schema.tagValues(
          bucket: "{bucket}",
          tag: "description",
          predicate: (r) => {predicate},
          start: -{time_range}
        )'''

        tables = self._perform_query(query=query)
        data = []
        for table in tables:
            for record in table.records:
                data.append(record.get_value())
        return data

    def get_values_count_combined(self, bucket, measurement=None, device_id=None, description=None,
                                  time_range=None, time_from=None, time_to=None,
                                  aggregate_window=None, aggregate_func=None) -> int:

        if time_range is None:
            time_range = 'all'

        tables = self._get_tables(bucket=bucket, measurement=measurement, device_id=device_id, description=description,
                                  time_range=time_range, time_from=time_from, time_to=time_to,
                                  aggregate_window=aggregate_window, aggregate_func=aggregate_func, count=True,
                                  keep_only_columns=["_value"])

        values_len = None
        for table in tables:
            for record in table.records:
                values_len = record.get_value()
        return values_len

    def get_values_count(self, bucket, measurement=None, device_id=None, description=None,
                         time_range=None, time_from=None, time_to=None,
                         aggregate_window=None, aggregate_func=None, window_count=None) -> dict:

        if time_range is None:
            time_range = '100y'

        local_vars = locals()
        local_vars.pop('self')
        local_vars['count'] = True
        local_vars['group_columns'] = ["device_id"]
        local_vars['keep_only_columns'] = ["_value", "device_id"]

        tables = self._get_tables(**local_vars)

        data = {}
        for table in tables:
            for record in table.records:
                data[record.values.get("device_id")] = record.get_value()
        return data

    def get_metadata(self, bucket, measurement=None, device_id=None, description=None,
                     time_range=None, time_from=None, time_to=None) -> list:
        """Get len and last value"""

        local_vars = locals()
        local_vars.pop('self')

        data = self.get_one_value(**local_vars)
        data_len = self.get_values_count(**local_vars)

        for item in data:
            device_id = item['device_id']
            if device_id in data_len:
                item['values_count'] = data_len[device_id]
            else:
                item['values_count'] = 0

        return data

    @staticmethod
    def pop_timestamp_from_values(data):
        return data['values'][-1][0]

    @staticmethod
    def to_one_value_format(data):
        # Transform data from tables to one value format:
        _data = []
        for item in data:
            item['timestamp'] = item['values'][-1][0]
            item['value'] = item['values'][-1][1]
            item.pop('values')
            _data.append(item)
        return _data

    def get_one_value(self, bucket, measurement=None, device_id=None, description=None,
                      time_range=None, time_from=None, time_to=None, sort='desc', last=True) -> list:
        """Get only one value per table (last or first)"""

        if time_range is None and time_from is None and time_to is None:
            time_range = 'all'

        tables = self._get_tables(bucket=bucket, measurement=measurement, device_id=device_id, description=description,
                                  time_range=time_range, time_from=time_from, time_to=time_to, last=last,
                                  first=not last, group_columns=["device_id"])

        data = self._extract_tables(tables)

        if sort == 'desc' or sort == 'asc':
            data.sort(key=self.pop_timestamp_from_values, reverse=sort == 'desc')

        return self.to_one_value_format(data)

    def get_values_from_device_id(self, bucket, measurement, device_id, description=None,
                                  time_range=None, time_from=None, time_to=None,
                                  aggregate_window=None, aggregate_func=None,
                                  sort='desc', limit=None, window_count=None):

        if measurement is None:
            raise ValueError("Invalid value for `measurement`, must not be `None`")

        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        local_vars = locals()
        local_vars.pop('self')
        local_vars['drop_columns'] = ["unit"]
        local_vars['keep_only_columns'] = ["_value", "_time"]

        tables = self._get_tables(**local_vars)

        values = self._extract_tables(tables)

        return values[0]['values'] if values else None

    def get_data_from_device_id(self, bucket, measurement, device_id, description=None,
                                time_range=None, time_from=None, time_to=None,
                                aggregate_window=None, aggregate_func=None,
                                sort='desc', limit=None, window_count=None) -> dict:

        if measurement is None:
            raise ValueError("Invalid value for `measurement`, must not be `None`")

        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")

        local_vars = locals()
        local_vars.pop('self')

        data = self.get_one_value(bucket=bucket,
                                  measurement=measurement,
                                  device_id=device_id,
                                  time_range=time_range,
                                  time_from=time_from,
                                  time_to=time_to,
                                  description=description)
        if data:
            data = data[0]
            data['values'] = self.get_values_from_device_id(**local_vars)
        else:
            data = {}
        return data

    def save_data(self, bucket, data, utc_to_local=False, timezone='Europe/Ljubljana', org=None):
        """ Save data to database

        sample_data = [{
            measurement: <str>,
            device_id: <str> (required),
            device: <str>,
            channel: <str>,
            description: <str>,
            unit: <str> (required),
            values: [[ <time>, value], ...] (required)
            timestamp: <time> (optional)
            value: <float> (optional)
        }]

        Note: timestamp must be saved without tzinfo, or it is removed

        :param bucket: Bucket
        :param data: Data to save (sample_data)
        :param org: Organisation
        :param utc_to_local: Convert time as utc to local time (timezone)
        :param timezone: Use timezone for utc conversion
        """

        if type(data) == dict:
            data = [data]

        if org is None:
            org = self.org

        tz = None
        if utc_to_local:
            tz = pytz.timezone(timezone)

        points = []
        for item in data:
            try:
                if not item['device_id']:
                    raise ValueError('Device id must be supplied')
                device_id = item['device_id']
                measurement = item.get('measurement', device_id.split('.')[0])
                device = item.get('device', measurement)
                channel = item.get('channel', device_id.split('.')[1])
                description = item.get('description', None)
                unit = item.get('unit', '')
                value = item.get('value', None)
                timestamp = item.get('timestamp', None)
                if 'values' not in item and timestamp is not None and value is not None:
                    item['values'] = [(timestamp, value)]

                for values in item['values']:
                    if type(values) not in [list, tuple]:
                        raise ValueError('Point must be `tuple` or `list` example: (2021-01-01 00:00:00, 1)')

                    dt = values[0]
                    value = float(values[1])

                    if type(dt) == str:
                        try:
                            dt = parse_datetime(dt)
                        except Exception:
                            logger.error(f"Invalid time string, ts:{dt}, data:{item}")
                            continue

                    if utc_to_local:
                        dt = localize_dt(dt)

                    if dt.year == 1970:
                        logger.error(f"Invalid timestamp error for year 1970, {measurement}:{device_id}")
                        continue

                    point = Point(measurement) \
                        .tag("device_id", device_id) \
                        .tag("device", device) \
                        .tag("channel", channel) \
                        .tag("unit", unit) \
                        .tag("timezone", timezone) \
                        .field("value", value) \
                        .time(time=dt)
                    if description is not None:
                        point.tag('description', description)
                    points.append(point)
            except Exception as e:
                logger.exception(e)
                logger.error(f"unable to write point, e:{e}")

        with self.write_api(write_options=WriteOptions(batch_size=500,
                                                       flush_interval=10_000,
                                                       jitter_interval=2_000,
                                                       retry_interval=5_000,
                                                       max_retries=5,
                                                       max_retry_delay=30_000,
                                                       exponential_base=2)) as _write_client:
            _write_client.write(bucket=bucket, org=org, record=points)

        if points:
            logger.info(f"written {len(points)} to database")

    def copy_from_to(self, bucket_from, measurement_from, devid_from, bucket_to, measurement_to, devid_to):
        data_from = self.get_data_from_device_id(bucket=bucket_from,
                                                 measurement=measurement_from,
                                                 device_id=devid_from,
                                                 time_range='100y')
        data_from['measurement'] = measurement_to
        data_from['device'] = measurement_to
        data_from['device_id'] = devid_to
        data_from['channel'] = ".".join(devid_to.split('.')[1:])

        self.save_data(bucket=bucket_to, data=data_from)

    def copy_bucket_to_bucket(self, bucket_from, bucket_to):
        query = 'from(bucket:"{bucket_from}") |> range(start: -1h)'

        records = self.query_api().query_stream(query)

        for record in records:
            print (record)
            # print(f'Temperature in {record["location"]} is {record["_value"]}')

    def _copy_data(self, bucket_from, bucket_to, org_to=None, measurement=None, device_id=None, description=None,
                   time_range=None, time_from=None, time_to=None, aggregate_window=None, aggregate_func=None,
                   sort='desc', limit=None):
        """Copy data from one bucket to another bucket"""

        if org_to is None:
            org_to = self.org

        if time_range is None:
            time_range = 'all'

        query = get_flux_query(bucket=bucket_from, bucket_to=bucket_to, org_to=org_to, measurement=measurement,
                               device_id=device_id, description=description,
                               time_range=time_range, time_from=time_from, time_to=time_to,
                               aggregate_window=aggregate_window,
                               aggregate_func=aggregate_func,
                               sort=None, limit=limit)
        self._perform_query(query)

    def move_data_to_trash(self, bucket, measurement, bucket_trash=None, device_id=None, description=None,
                           time_range=None, time_from=None, time_to=None, delete_afterwords=True):

        if measurement is None:
            raise ValueError("Invalid value for `measurement`, must not be `None`")

        if bucket_trash is None:
            bucket_trash = f'{bucket}_trash_{datetime.now().year}'

        bucket_api = self.buckets_api()
        if not bucket_api.bucket_exists(bucket_name=bucket_trash):
            org = self.organizations_api().get_organization(org_name=self.org)
            bucket_api.create_bucket(bucket_name=bucket_trash, org=org,
                                     description=f"Trash bucket for year {datetime.now().year}")

        self._copy_data(bucket_from=bucket, bucket_to=bucket_trash, measurement=measurement, device_id=device_id,
                        description=description, time_range=time_range, time_from=time_from, time_to=time_to)

        if delete_afterwords:
            device_ids = [device_id] if device_id is not None else []
            descriptions = [description] if description is not None else []
            self.delete_api().delete_data(bucket=bucket, measurements=[measurement], device_ids=device_ids,
                                          descriptions=descriptions, org=self.org,
                                          time_from=time_from, time_to=time_to)

    def count_data_in_buckets(self):
        buckets = self.buckets_api().list_buckets(only_names=True)
        counts = {}
        for bucket in buckets:
            count = self.get_values_count_combined(bucket=bucket)
            if count is None:
                count = 0
            counts[bucket] = count
        return dict(sorted(counts.items(), key=lambda item: item[1]))

    def save_dtv_data(self, filepath, device_id, bucket):
        if device_id is None:
            raise ValueError("Argument `devid` must not be None.")
        with open(filepath, 'rb') as f:
            file = f.read()
            data = self.parse_dtv_bytes(file)
            print(data)
        data_write = {
            "measurement": device_id.split('.')[0],
            "device_id": device_id,
            "values": data['values'],
            "unit": data['unit']
        }
        self.save_data(bucket=bucket, data=data_write)

    def parse_dtv_bytes(self, file: bytes) -> dict:
        """
        :param file: File that has dtv styling
        :return: {unit:<unit>, data:[<timestamp>,<value>]}
        """

        lines = file.decode().split('\n')

        # Retrieve unit
        unit = ''
        for line in lines[0:8]:
            item = line.strip()
            if item != '':
                unit = item

        # Retrieve data
        values = []
        for line in lines:
            item = line.split(',')
            if len(item) == 2:
                try:
                    ts = item[0].strip()
                    val = float(item[1].strip())
                    if '.' in ts:
                        dt = datetime.strptime(ts, "%d/%m/%Y %H:%M:%S.%f")
                    else:
                        dt = datetime.strptime(ts, "%d/%m/%Y %H:%M:%S")
                except ValueError as e:
                    logger.exception(e)
                    # Invalid datetime string
                    continue
                values.append((dt, val))

        return {"unit": unit, "values": values}


