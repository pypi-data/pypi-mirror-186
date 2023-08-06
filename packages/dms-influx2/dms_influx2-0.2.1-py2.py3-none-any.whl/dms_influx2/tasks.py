from influxdb_client import TasksApi


class Tasks(TasksApi):
    def __init__(self, client):
        self.org = client.org
        self.org_id = client.organizations_api().get_organization(org_name=self.org)
        super().__init__(client)

    def create_or_update_calibration_task(self,
                                          bucket,
                                          measurement,
                                          channel_src,
                                          channel_dest,
                                          const_a=None,
                                          const_b=None,
                                          const_c=None,
                                          const_d=None,
                                          offset=None,
                                          altitude=None,
                                          baro_url=None,
                                          baro_allowed_hours_diff=12,
                                          task_id=None):
        if bucket is None:
            raise ValueError('Value for argument `bucket` must not be None')
        if measurement is None:
            raise ValueError('Value for argument `measurement` must not be None')
        if channel_src is None:
            raise ValueError('Value for argument `channel_src` must not be None')
        if channel_dest is None:
            raise ValueError('Value for argument `channel_dest` must not be None')
        if const_a is None:
            const_a = 0
        if const_b is None:
            const_b = 0
        if const_c is None:
            const_c = 1
        if const_d is None:
            const_d = 0
        if offset is None:
            offset = 0
        if altitude is None:
            altitude = 0
        if baro_allowed_hours_diff is None:
            baro_allowed_hours_diff = 12

        const_a = float(const_a)
        const_b = float(const_b)
        const_c = float(const_c)
        const_d = float(const_d)
        offset = float(offset)
        altitude = float(altitude)

        name = f'calibration_{bucket}_{measurement}_{channel_src}_{channel_dest}'

        if baro_url and baro_allowed_hours_diff:
            header = f'response = requests.get(url: "{baro_url}", params: ["allowed_hours_diff": ["{baro_allowed_hours_diff}"]])\n'\
                     f'valueH = json.parse(data: response.body)["value_h"]\n' \
                     f'measurement = if response.statusCode == 200 then "{measurement}" else ""'
        else:
            header = f'measurement = "{measurement}"\n' \
                     f'valueH = 0.0'

        value = f'math.round(x: ({const_a} * math.pow(x: r._value, y: 3.0) + {const_b} * math.pow(x: r._value, y: 2.0) + ' \
                f'{const_c} * math.pow(x: r._value, y: 1.0) + {const_d} + {offset} + {altitude} - valueH) * 1000.0) / 1000.0'

        flux = f'{header}\n' \
               f'from(bucket: "{bucket}")\n' \
               f'|> range(start: -task.every)\n' \
               f'|> filter(fn: (r) => r._measurement == measurement)\n' \
               f'|> filter(fn: (r) => r["_field"] == "value")\n' \
               f'|> filter(fn: (r) => r["channel"] == "{channel_src}")\n' \
               f'|> map(fn: (r) => ({{r with _value: {value} }}))\n' \
               f'|> map(fn: (r) => ({{r with channel: "{channel_dest}", device_id: "${{r.device}}.{channel_dest}"}}))' \
               f'|> to(bucket: "{bucket}")'
        print(flux)
        if task_id is not None:
            task = self.find_task_by_id(task_id=task_id)
        else:
            task = self.create_task_every(name=name, flux=flux, organization=self.org_id, every='1m')

        task.flux = 'import "math"\n'\
                    'import "http/requests"\n' \
                    'import "experimental/json"\n'\
                    f'option task = {{name: "{name}", every: 1m}} \n' + flux
        return self.update_task(task)
