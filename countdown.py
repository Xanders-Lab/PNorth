import datetime

def countdown(target_date_time):
    target_datetime = datetime.datetime.strptime(target_date_time, '%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.datetime.now()

    time_delta = target_datetime - current_datetime

    days = time_delta.days
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

# Example usage
target_date_time = '2023-12-01 00:00:00'
time_remaining = countdown(target_date_time)
print(f'Time remaining until {target_date_time}: {time_remaining}')
