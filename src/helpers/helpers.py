import datetime
from json import JSONEncoder
import dateutil.parser


# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, objs):
            for obj in objs:
                if isinstance(obj, (datetime.date, datetime.datetime)):
                    objs.append(obj.isoformat())

            return objs


# custom Decoder
def DecodeDateTime(empDict):
    if 'created_at' in empDict:
      empDict["created_at"] = dateutil.parser.parse(empDict["created_at"])

    if 'updated_at' in empDict:
      empDict["updated_at"] = dateutil.parser.parse(empDict["updated_at"])

    return empDict