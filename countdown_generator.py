import datetime

def calculate_countdown(target_date):
    current_datetime = datetime.datetime.now()
    
    time_remaining = target_date - current_datetime
    
    
    days = time_remaining.days
    print(days)
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds


year = int(input("Enter the target year: "))
month = int(input("Enter the target month: "))
day = int(input("Enter the target day: "))
target_date = datetime.datetime(year, month, day)


days, hours, minutes, seconds = calculate_countdown(target_date)


print("Countdown:")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
