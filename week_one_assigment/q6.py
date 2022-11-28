import time
date_time_stamp = time.asctime().replace(':', '.')
current_time = float(date_time_stamp[11:16])
print(f"The time is {current_time}")
if current_time >= 5.30 and current_time < 10.00:
    print("Good morning!")
elif current_time >= 10.00 and current_time < 17.00:
    print("Good day!")
elif current_time >= 17.00 and current_time < 22.00:
    print("Good evening!")
else:
    print("Go to bed!")
