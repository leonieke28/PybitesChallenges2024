import os
import urllib.request
from datetime import datetime

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """
    Extract timestamp from logline and convert it to a datetime object.
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
    datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp_str = line.split()[1]
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    """
    Extract shutdown events ("Shutdown initiated") from loglines and
    calculate the timedelta between the first and last one.
    Return this datetime.timedelta object.
    """
    shutdowns = []
    for line in loglines:
        if line.endswith("Shutdown initiated.\n"):
            shutdowns.append(convert_to_datetime(line))

    calculated_timedelta = shutdowns[1] - shutdowns[0]
    return calculated_timedelta
