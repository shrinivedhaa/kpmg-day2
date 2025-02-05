from datetime import datetime, timedelta, timezone

# 1. Get the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# 2. Format the date and time
formatted_date = current_datetime.strftime("%d-%m-%Y")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# 3. Parse a string into a datetime object
date_string = "27-01-2025 15:45:30"
parsed_datetime = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)

# 4. Add or subtract time using timedelta
next_week = current_datetime + timedelta(weeks=1)
yesterday = current_datetime - timedelta(days=1)
print("One Week Later:", next_week)
print("Yesterday:", yesterday)

# 5. Calculate the difference between two dates
date1 = datetime(2025, 1, 27)
date2 = datetime(2025, 2, 3)
date_difference = date2 - date1
print(date_difference)
print("Difference Between Dates:", date_difference.days, "days")

# 6. Handling time zones
utc_now = datetime.now(timezone.utc)
print(timezone.utc)
print("UTC Time:", utc_now)

# Convert UTC to a different timezone
# For this example, we'll use IST (Indian Standard Time: UTC+5:30)
ist_offset = timedelta(hours=5, minutes=30)
ist_time = utc_now.astimezone(timezone(ist_offset))
print("IST Time:", ist_time)

# 7. Get only date or time
current_date = current_datetime.date()
current_time = current_datetime.time()
print("Current Date:", current_date)
print("Current Time:", current_time)
