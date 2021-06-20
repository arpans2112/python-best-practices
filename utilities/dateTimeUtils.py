import datetime


def getnowdatetimestf():
    now_date = datetime.datetime.now().strftime("%x").replace("/", "_")
    now_time = datetime.datetime.now().strftime("%X").replace(":", "_")
    return now_date + '_' + now_time
