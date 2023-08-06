import time
import datetime
import tqdm
from dateutil.parser import parse as dateparser
from dateutil.parser import ParserError

try:
    from . import Re
except:
    import Re

def FormatDuration(seconds:int) -> str:
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

Now = time.time 

def Sleep(num:int=0, title:str=None, bar:bool=None):
    """
    Sleep(num:int, bar:bool=None)
    
    The first argument is an integer, and the second argument is a boolean. The second argument is
    optional, and if it is not provided, it will be set to True if the first argument is greater than 5,
    and False otherwise
    
    :param num: The number of seconds to sleep
    :type num: int
    :param bar: If True, a progress bar will be displayed. If False, no progress bar will be displayed.
    If None, a progress bar will be displayed if the number of seconds is greater than 5
    :type bar: bool
    """
    if num == 0:
        while True:
            time.sleep(333)
    else:
        if bar == None:
            if num > 5:
                bar = True 
            else:
                bar = False

        if bar:
            num = int(num)
            for _ in tqdm.tqdm(range(num), total=num, leave=False, desc=title):
                time.sleep(1)
        else:
            time.sleep(num)

def Strftime(timestamp:float|int, format:str="%Y-%m-%d %H:%M:%S") -> str:
    """
    It converts a timestamp to a string.
    
    :param format: The format string to use
    :type format: str
    :param timestamp: The timestamp to format
    :type timestamp: float|int
    :return: A string
    """
    dobj = datetime.datetime.fromtimestamp(timestamp)
    return dobj.strftime(format)

def parseTimeago(timestring:str) -> int|None:
    if timestring == "just now":
        return int(Now())
    
    res = Re.FindAll('([0-9]+)([smhdw])', timestring)
    # print(res)
    if len(res) != 0:
        sm = {
            "s": "second",
            "m": "minute",
            "h": "hour",
            "d": "day",
            "w": "week",
        }
        timestring = res[0][1] + " " + sm[res[0][2]] + " ago"

    formates = [
        "([0-9]+) %ss{0,1} ago",
        "in ([0-9]+) %ss{0,1}",
        "([0-9]+) %s\. ago"
    ]

    step = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2592000,
        "mo": 2592000,
        "year": 31536000,
        "yr": 31536000,
    }

    for s in step:
        for f in formates:
            f = f % s 

            res = Re.FindAll(f, timestring)
            if len(res) != 0:
                duration = step[s]
                num = int(res[0][1])

                return int(Now()) - duration * num 
    
    return None

def Strptime(timestring:str, format:str=None) -> int:
    """
    It takes a string of a date and time, and a format string, and returns the Unix timestamp of that
    date and time
    
    :param format: The format of the timestring
    :type format: str
    :param timestring: The string to be converted to a timestamp
    :type timestring: str
    :return: The timestamp of the datetime object.
    """

    if format:
        dtimestamp = datetime.datetime.strptime(timestring, format).timestamp()
    else:
        if len(Re.FindAll('([0-9]+)([smhdw])', timestring)) != 0:
            dtimestamp = parseTimeago(timestring)
            if not dtimestamp:
                raise Exception(f"不能解析时间字符串: {timestring}")
        else:
            try:
                dtimestamp = dateparser(timestring).timestamp()
            except ParserError as e:
                dtimestamp = parseTimeago(timestring)
                if not dtimestamp:
                    raise Exception(f"不能解析时间字符串: {timestring}")

    return int(round(dtimestamp))

if __name__ == "__main__":
    # print(Strptime("2022-05-02 23:34:10", "%Y-%m-%d %H:%M:%S"))
    # print(Strftime(1651520050, "%Y-%m-%d %H:%M:%S"))
    # print(Strftime(Now()))
    # print(Strptime("2017-05-16T04:28:13.000000Z"))

    # print(Strptime("6 months ago"))
    # print(Strftime(Strptime("6 months ago")))
    # print(Strptime("just now"))
    # print(Strftime(Strptime("just now")))
    # print(Strptime("1 second ago"))
    # print(Strftime(Strptime("1 second ago")))
    # print(Strptime("in 24 days"))
    # print(Strftime(Strptime("in 24 days")))

    # print(FormatDuration(1750))
    # print(Strftime(Strptime("4m"))) # 4分钟前
    # print(Strftime(Strptime("2h"))) # 2小时前

    print(Strftime(Strptime("3 mo. ago"))) # 3个月前
    print(Strftime(Strptime("3 yr. ago"))) # 3年前