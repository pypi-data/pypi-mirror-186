from datetime import datetime, timezone, timedelta
from one_interfaces import jsonTicksDateTime_pb2 as jsonTicksTime


def GetRowNumber(date: datetime, wsType):
    if not date.tzinfo:
        date = date.replace(tzinfo=timezone.utc)
    BaseTime = datetime(1900, 1, 1, 0, 0, 0, 0, timezone.utc)
    diffTime = date - BaseTime
    windowSize = TimeSpanOfWorksheetType(wsType)
    diffTimeMinutes = diffTime.total_seconds()/60
    windowSizeMinutes = windowSize.total_seconds()/60
    return int(diffTimeMinutes / windowSizeMinutes) + 1


def GetDateFromRowNumber(rowNumber, wsType):
    BaseTime = datetime(1900, 1, 1, 0, 0, 0, 0, timezone.utc)
    row = rowNumber-1
    windowSize = TimeSpanOfWorksheetType(wsType)
    windowSizeMinutes = windowSize.total_seconds()/60
    mins = windowSizeMinutes*row
    return BaseTime+timedelta(minutes=mins)


def ToJsonTicksDateTime(date: datetime):
    jsTime = jsonTicksTime.JsonTicksDateTime()
    jsTime.jsonDateTime.value = str(date)
    return jsTime


def TimeSpanOfWorksheetType(wsType):
    if wsType == 1:
        return timedelta(minutes=15)
    elif wsType == 2:
        return timedelta(hours=1)
    elif wsType == 3:
        return timedelta(hours=4)
    elif wsType == 4:
        return timedelta(days=1)
    else:
        return "Invalid worksheet type"
