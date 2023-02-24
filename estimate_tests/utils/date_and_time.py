from datetime import datetime


current_date = str(datetime.today().date())

current_time = str(datetime.now().strftime("%H:%M"))

today_date = str(datetime.today().strftime('%Y-%m-%d-%H-%M'))

current_time_with_sec = str(datetime.now())

print(current_time_with_sec,'!', today_date, '!', current_time, '!', current_date)