import datetime

def get_day_range(current:datetime.datetime, day_shift:int, duration:int):
    duration = duration if duration > 0 else 1
    today = current.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = today + datetime.timedelta(days=day_shift)
    end_date = start_date + datetime.timedelta(days=duration-1)
    return start_date, end_date

def datetime_to_str(dates):
    return tuple([dt.strftime("%Y-%m-%d") for dt in dates])

def normalize_date_range(date_range:str)->str:
    result = date_range.replace("-", "")
    result = result.replace("_", "")
    result = result.lower()
    return result

def parse_date_range(date_range):
    """
    LAST_MONTH@1
    """
    if "@" in date_range:
        date_range, shift = date_range.split("@")
        shift = int(shift)
    else:
        shift = 0
    return date_range, shift

def get_month_dates_by_param(date_range:str, shift=0):
    """
    Obsolete, to be deleted.
    """
    today = datetime.datetime.today()
    return get_date_range_by_param(today, date_range, shift)

def get_date_range_by_param(today:datetime.datetime, date_range:str, shift=0):
    date_range, shift_in_line = parse_date_range(date_range)
    shift = shift_in_line + shift
    date_range = normalize_date_range(date_range)
    dates_map = {
        "lastday": datetime_to_str(get_day_range(today,-1-shift,1)),
        "lastweek": get_week_range(today, -1-shift),
        "thismonth": get_this_month_range(today), 
        "lastmonth": get_month_valid_range(today, -1-shift),
        "lastyear": get_date_range_for_last_year(today),
        "last3months": get_date_range_for_last_n_months(today, 3),
        "last6months": get_date_range_for_last_n_months(today, 6,-shift)    
    }
    if date_range in dates_map:
        return dates_map[date_range]
    else:
        return get_date_range_for_days(today, date_range)

def get_date_range_for_last_year(current:datetime.datetime):
    today = current
    start_date = today.replace(year=today.year-1, day=1)
    end_date = today.replace(day=1) - datetime.timedelta(days=1)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")

def get_date_range_for_last_n_months(current:datetime.datetime, n:int, shift:int=0):
    today = current
    if shift>0:
        shift=0
    for i in range(-shift):
        today = last_month(today)
    start_date = today.replace(day=1)
    for i in range(n):
        start_date = last_month(start_date)
    end_date = today.replace(day=1) - datetime.timedelta(days=1)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")    

def get_date_range_for_days(current:datetime.datetime, days:str):
    if days.isdigit():
        days = int(days)
    else:
        days = 0
    # today = datetime.datetime.today()
    start_date = current - datetime.timedelta(days=days)
    return start_date.strftime("%Y-%m-%d"), current.strftime("%Y-%m-%d")

def next_month(dt):
    return (dt.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)

def last_month(dt):
    return (dt.replace(day=1) - datetime.timedelta(days=2)).replace(day=1)

def get_report_period(date_range:str, execution_date:str)->str:
    current = datetime.datetime.now()
    if execution_date:
        try:
            current = datetime.datetime.strptime(execution_date,"%Y-%m-%d")
        except ValueError:
            pass
    start_date, _ = get_date_range_by_param(current, date_range)
    return start_date[:7]

def get_week_range_for_month(dt)->list:
    '''
    get week range for a month, from the last Monday to the next Sunday. 
    Make sure all weeks included for current month.
    '''
    day1 = dt.replace(day=1)
    next_month_day1 = next_month(dt)
    last_monday = day1 + datetime.timedelta(days=(7-day1.weekday())%7, weeks=-1)
    next_sunday = next_month_day1 + datetime.timedelta(days=-(next_month_day1.weekday()+1), weeks=1)
    weeks = []
    day = last_monday
    while day < next_sunday:
        weeks.append([day, day+datetime.timedelta(days=6)])
        day = day + datetime.timedelta(weeks=1)
    return weeks

def get_week_range(current:datetime.datetime, shift=0, week_start=-1):
    # current = datetime.datetime.today()
    if shift > 0:
        for i in range(1,shift+1):
            current = current + datetime.timedelta(weeks=1)
    elif shift < 0:
        for i in range(shift,0):
            current = current - datetime.timedelta(weeks=1)
    start_date = current - datetime.timedelta(days=current.weekday())+datetime.timedelta(days=week_start)
    end_date = start_date + datetime.timedelta(days=6)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")

def get_month_valid_range(current:datetime.datetime, shift=0):
    if shift > 0:
        shift = 0
    # current = datetime.datetime.today()
    for i in range(shift,0):
        current = last_month(current)
    start_date = current.replace(day=1).strftime("%Y-%m-%d")
    end_date_value = next_month(current) - datetime.timedelta(days=1)
    end_date_value = datetime.datetime.today() if end_date_value > datetime.datetime.today() else end_date_value
    end_date = end_date_value.strftime("%Y-%m-%d")
    return start_date, end_date

def get_this_month_range(current:datetime.datetime, shift:int=1):
    """
    Shift days for this month.
    """
    # current = datetime.datetime.today()
    return get_month_valid_range(current, -1) if current.day <= shift else get_month_valid_range(current)  

def get_month_dates(current:datetime.datetime, shift=0):
    current = current.replace(day=1)
    if shift >0:
        for i in range(1,shift+1):
            current = next_month(current)
    elif shift <0:
        for i in range(shift,0):
            current = last_month(current)
    start_date = current.strftime("%Y-%m-%d")
    end_date = (next_month(current) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return start_date, end_date

def get_date_format(locale:str):
    locale = locale.replace("-", "_")
    format_map = {
        "en_US": "%m/%d/%Y",
        "en_CA":"%Y-%m-%d",
        "en_DE": "%d/%m/%Y",
        "en_GB": "%d/%m/%Y"
    }
    if locale not in format_map:
        locale = "en_US" 
    return format_map[locale] 