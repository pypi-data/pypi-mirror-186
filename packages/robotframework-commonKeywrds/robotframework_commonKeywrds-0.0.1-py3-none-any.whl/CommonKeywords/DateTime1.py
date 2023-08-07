""" Fetch CST time """
from datetime import datetime
from pytz import timezone


def getcurrentDateTimeZone(TimeZone, Format):
    """
                helper function to get the Current Date
    """
    Current_Date = datetime.now(timezone(TimeZone)).strftime(Format)
    return Current_Date


def currentDateTime():
    """
                helper function to get the Current DateTime
    """
    Current_Time = datetime.now(timezone('America/Chicago')).strftime("%Y-%m-%d %H:%M:%S")
    return Current_Time


def currenttimefordiffzones(timeZone):
    """
                helper function to get the currenttimefordiffzones
                """
    currenttime = datetime.now(timezone(timeZone)).strftime("%H:%M:%S")
    if timeZone == "America/Chicago":
        currenttimewithzone = currenttime + ' ' + "CDT"
    elif timeZone == "America/New_York":
        currenttimewithzone = currenttime + ' ' + "EDT"
    if timeZone == "America/Anchorage":
        currenttimewithzone = currenttime + ' ' + "AKDT"
    elif timeZone == "Pacific/Honolulu":
        currenttimewithzone = currenttime + ' ' + "HST"
    if timeZone == "America/Phoenix":
        currenttimewithzone = currenttime + ' ' + "MST"
    elif timeZone == "America/Los_Angeles":
        currenttimewithzone = currenttime + ' ' + "PDT"

    return currenttimewithzone


def current_date_time1():
    """
                helper function to get the Current Date1
                """
    Current_Time = datetime.now(timezone('America/Chicago')).strftime("%Y-%m-%d")
    return Current_Time


def epochtimeToTZ(epoch_time, TimeZone, datetimeformat):
    tz = timezone(TimeZone)  # 'America/Chicago'
    dt = datetime.fromtimestamp(epoch_time, tz)
    # print it
    print(dt.strftime(datetimeformat))  # '%m/%d/%Y %H:%M'
    return dt.strftime(datetimeformat)


class DateTime:
    """ Connection class """

    def __init__(self):
        self.log = None

    def currentDateTimeNew(self):
        self.log = None
        Current_TimeNew = datetime.now(timezone('America/Chicago')).strftime("%Y-%m-%d")
        return Current_TimeNew

    @staticmethod
    def Difference():
        """ Fetch CST timings """

    shift = "Shift1".upper()
    if shift == "Shift1".upper():
        start = "00:00:00"
        end = "11:59:00"
    elif shift == "Shift2".upper():
        start = "12:00:00"
        end = "23:59:00"
    elif shift == "Shift3".upper():
        start = "12:00:00"
        end = "14:59:00"
    elif shift == "Production Day".upper():
        start = "00:00:00"
        end = "24:00:00"

    Now = datetime.now(timezone('America/Chicago')).strftime("%H:%M:%S")

    Current_Time = datetime.strptime(Now, "%H:%M:%S")  # Converting string to date
    print("Current Time(CST):", Current_Time)

    start_time = datetime.strptime(start, "%H:%M:%S")
    print("Shift Start Time:", start_time)

    total_time = str(Current_Time - start_time)
    print("TotalTime:", total_time)

    hours, minutes, seconds = map(int, total_time.split(':'))
    CurrentTimeInSec1 = (hours * 3600 + minutes * 60 + seconds)
    print("Max Run time:", CurrentTimeInSec1)


if __name__ == "__main__":
    TEST = DateTime()
