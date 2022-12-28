# filter.py : 날짜 및 시간 format

def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)