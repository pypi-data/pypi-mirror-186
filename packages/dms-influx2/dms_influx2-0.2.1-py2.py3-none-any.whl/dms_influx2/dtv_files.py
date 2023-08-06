import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def parse_dtv_bytes(file: bytes) -> dict:
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


def create_dtv_file(device, channel, unit, values):
    lines = ['\n', '\n', unit, '\n', '\n', '\n', '\n', '\n', '\n', '\n']
    filename = f'{device}_{channel}.dtv'
    for dt, value in values:
        ts = dt.replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")
        lines.append(f'{ts},{value}\n')
    with open(filename, 'w') as f:
        f.writelines(lines)
    return filename
