from datetime import datetime, timedelta
date = datetime(2020, 10, 10, 12, 7, 23)
x = 0
while x < 10:
    print(date)
    date = date+timedelta(days=14)
    x = x+1

