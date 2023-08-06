import json
from datetime import datetime

from dms_influx2.utils import timestamp_to_influx_string, localize_dt


def get_flux_query(bucket=None,
                   measurement=None,
                   device_id=None,
                   description=None,
                   time_range='1h',
                   time_from=None,
                   time_to=None,
                   aggregate_window=None,
                   aggregate_func=None,
                   sort=None,
                   count=None,
                   last=False,
                   first=False,
                   limit=None,
                   drop_columns=None,
                   keep_only_columns=None,
                   group_columns=None,
                   distinct=False,
                   field='value',
                   bucket_to=None,
                   org_to=None,
                   time_shift=None,
                   time_offset: int = None,
                   window_count: str = None) -> str:
    """

    :param first:
    :param window_count:
    :param time_offset:
    :param time_shift:
    :param field:
    :param bucket: Name of the bucket
    :param measurement: Name of the measurement
    :param device_id: ID of device
    :param description: Description of data set
    :param time_range:
    :param time_from:
    :param time_to:
    :param aggregate_window:
    :param aggregate_func:
    :param sort:
    :param count:
    :param last:
    :param limit:
    :param drop_columns:
    :param keep_only_columns:
    :param group_columns:
    :param distinct:
    :param bucket_to:
    :param org_to:
    :return:
    """

    if bucket is None:
        raise ValueError("Invalid value for `bucket`, must not be `None`")

    stop = None

    if time_range == 'all':
        time_range = '100y'

    if time_range is not None:
        start = f"-{time_range}"
    else:
        start = "-1h"

    if time_from is not None:
        start = timestamp_to_influx_string(time_from, time_offset)

    if time_to is not None:
        stop = timestamp_to_influx_string(time_to, time_offset)

    if field is None:
        field = 'value'

    if time_shift is not None:
        now = timestamp_to_influx_string(localize_dt(datetime.utcnow()))
    else:
        now = timestamp_to_influx_string(datetime.utcnow())

    # Set now if local timestamp is used
    query_str = f'option now = () => {now}'

    query_str += f'\n\tfrom(bucket:"{bucket}")'
    if stop:
        query_str += f'''\n\t|> range(start: {start}, stop:{stop})'''
    else:
        query_str += f'''\n\t|> range(start: {start})'''

    if measurement:
        query_str += f'''\n\t|> filter(fn: (r) => r["_measurement"] == "{measurement}")'''

    if device_id:
        query_str += f'''\n\t|> filter(fn: (r) => r["device_id"] == "{device_id}")'''

    if description:
        query_str += f'''\n\t|> filter(fn: (r) => r["description"] == "{description}")'''

    query_str += f'''\n\t|> filter(fn: (r) => r["_field"] == "{field}")'''

    if aggregate_window:
        if type(aggregate_window) != str:
            raise ValueError("Invalid type for `aggregate_window`, must be type `str`")
        if aggregate_func is None:
            aggregate_func = "mean"
        query_str += f'''\n\t|> aggregateWindow(every: {aggregate_window}, fn: {aggregate_func}, createEmpty: false)'''

    if window_count is not None:
        if type(window_count) != str:
            raise ValueError("Invalid type for `window_count`, must be type `str`")
        query_str += f'''\n\t|> window(every: {window_count}, createEmpty: true)'''
        query_str += f'''\n\t|> count()'''
        query_str += f'''\n\t|> rename(columns: ''' + '{_stop: "_time"})'
        query_str += f'''\n\t|> group(columns: ["_measurement", "device_id"], mode:"by")'''

    if group_columns:
        if type(group_columns) != list:
            raise ValueError("Invalid type for `group_columns`, must be type `list`")
        query_str += f'''\n\t|> group(columns: {json.dumps(group_columns)})'''

    if drop_columns:
        if type(drop_columns) != list:
            raise ValueError("Invalid type for `drop_columns`, must be type `list`")
        query_str += f'''\n\t|> drop(columns: {json.dumps(drop_columns)})'''

    if keep_only_columns:
        if type(keep_only_columns) != list:
            raise ValueError("Invalid type for `keep_only`, must be type `list`")
        query_str += f'''\n\t|> keep(columns: {json.dumps(keep_only_columns)})'''

    if count:
        query_str += f'''\n\t|> count(column: "_value")'''

    if sort is not None:
        # TODO: better sorting system
        # It appears that sort is very slow and cpu intensive
        if sort not in ['asc', 'desc']:
            raise ValueError("Invalid value for `sort`, must not be `asc` or `desc`")
        desc = "true" if sort == 'desc' else "false"
        query_str += f'''\n\t|> sort(columns: ["_time"], desc: {desc})'''

    if last:
        query_str += '''\n\t|> last()'''

    if first:
        query_str += '''\n\t|> first()'''

    if limit is not None:
        query_str += f'''\n\t|> limit(n:{limit}, offset: 0)'''

    if distinct:
        query_str += f'''\n\t|> distinct()'''

    if time_shift is not None:
        query_str += f'''\n\t|> timeShift(duration: {time_shift})'''

    if bucket_to is not None and org_to is not None:
        query_str += f'''\n\t|> to(bucket: "{bucket_to}", org: "{org_to}")'''

    return query_str
