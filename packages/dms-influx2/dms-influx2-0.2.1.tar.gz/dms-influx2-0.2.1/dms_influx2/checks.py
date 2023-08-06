from datetime import datetime
from typing import List

from influxdb_client import ChecksService, LesserThreshold, CheckStatusLevel, ThresholdCheck, DashboardQuery, \
    QueryEditMode, TaskStatusType, DeadmanCheck
from influxdb_client.rest import ApiException

from dms_influx2.exceptions import CheckError
from dms_influx2.utils import timestamp_to_influx_string, localize_dt


class ChecksApi(ChecksService):
    def __init__(self, client):
        self.org = client.org
        self.org_id = client.organizations_api().get_id_organization_by_name(self.org)
        super().__init__(api_client=client.api_client)

    def get_all_checks(self):
        return self.get_checks(org_id=self.org_id)

    def create_threshold_check(self,
                               check_name,
                               bucket_name,
                               measurement,
                               device_id,
                               thresholds: List,
                               check_id=None,
                               **kwargs):
        now = timestamp_to_influx_string(localize_dt(datetime.utcnow()))
        query = f'''
            option now = () => {now}
            from(bucket: "{bucket_name}")
              |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
              |> filter(fn: (r) => r["_measurement"] == "{measurement}")
              |> filter(fn: (r) => r["device_id"] == "{device_id}")
              |> filter(fn: (r) => r["_field"] == "value")
              |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
              |> yield(name: "mean")
        '''

        # Due to the bug in influx api we cannot post '0' as value for any of the thresholds
        # Easy fix is to replace 0 with 0.0001 which is almost like zero. Nobody will know the difference
        for threshold in thresholds:
            for key, val in threshold.items():
                try:
                    if float(val) == float(0):
                        threshold[key] = 0.0001
                except ValueError:
                    pass

        check = ThresholdCheck(name=f"{check_name}",
                               status_message_template="The value is on: ${ r._level } level!",
                               every="5s",
                               offset="0s",
                               query=DashboardQuery(edit_mode=QueryEditMode.ADVANCED, text=query),
                               thresholds=thresholds,
                               org_id=self.org_id,
                               status=TaskStatusType.ACTIVE)
        try:
            if check_id is not None:
                return self.put_checks_id(check_id=check_id, check=check)
            else:
                return self.create_check(check)
        except ApiException as e:
            if e.status == 422:
                raise CheckError(f"Check with name {check_name} already exists.")

    def create_deadmancheck(self,
                            check_name: str,
                            bucket_name: str,
                            measurement: str,
                            device_id: str,
                            time_since: str,
                            stale_time: str,
                            level: str,
                            check_id=None,
                            **kwargs):
        """
        Trigger when values are not reporting for <time_since> and stop checking after <stale_time>.
        Set status to <level>.
        if check_id is passed than make an update

        :param time_since: 90s or 120m, or 2h
        :param stale_time: 90s or 120m, or 2h
        :param level: CRIT, INFO, WARN, OK
        :return: created check
        """

        now = timestamp_to_influx_string(localize_dt(datetime.utcnow()))
        query = f'''
            option now = () => {now}
            from(bucket: "{bucket_name}")
              |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
              |> filter(fn: (r) => r["_measurement"] == "{measurement}")
              |> filter(fn: (r) => r["device_id"] == "{device_id}")
              |> filter(fn: (r) => r["_field"] == "value")
              |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
              |> yield(name: "mean")
        '''
        check = DeadmanCheck(name=f"{check_name}",
                             status_message_template="The value is on: ${ r._level } level!",
                             every="5s",
                             offset="0s",
                             query=DashboardQuery(edit_mode=QueryEditMode.ADVANCED, text=query),
                             time_since=time_since,
                             stale_time=stale_time,
                             org_id=self.org_id,
                             level=level,
                             status=TaskStatusType.ACTIVE)
        try:
            if check_id is not None:
                return self.put_checks_id(check_id=check_id, check=check)
            else:
                return self.create_check(check)
        except ApiException as e:
            if e.status == 422:
                raise CheckError(f"Check with name {check_name} already exists.")

    def check_id_exists(self, check_id):
        try:
            self.get_checks_id(check_id=check_id)
            return True
        except ApiException as e:
            if e.status == 404 or e.status == 400:
                return False
