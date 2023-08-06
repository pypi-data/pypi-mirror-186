import datetime
import json
import pathlib

import easyuri


def dump(payload, **kwargs):
    path = kwargs.pop("path", None)
    output = JSONEncoder(**kwargs).encode(payload)
    if path is None:
        return output
    with pathlib.Path(path).open("w") as fp:
        fp.write(output)


def load(payload=None, path=None):
    if path:
        with pathlib.Path(path).open("r") as fp:
            return json.load(fp)
    elif payload:
        return json.loads(payload)


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, easyuri.URI):
            return str(obj)
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return {
                "datetime": obj.in_tz("utc").isoformat(),
                "timezone": obj.timezone.name,
            }
        return json.JSONEncoder.default(self, obj)
