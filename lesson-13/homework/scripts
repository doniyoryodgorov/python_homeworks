from datetime import datetime, timedelta
import re
import pytz
import time
#TASK 1
# Age Calculator
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
today = datetime.today()
age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
age_months = (today.month - birthdate.month - (today.day < birthdate.day)) % 12
age_days = (today - birthdate.replace(year=today.year, month=today.month)).days
print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

#TASK 2
# Days Until Next Birthday
next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_until_birthday = (next_birthday - today).days
print(f"Days until your next birthday: {days_until_birthday}")

#TASK 3
# Meeting Scheduler
current_dt_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_hours = int(input("Enter duration hours: "))
duration_minutes = int(input("Enter duration minutes: "))
current_dt = datetime.strptime(current_dt_str, '%Y-%m-%d %H:%M')
end_meeting = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
print(f"Meeting ends at: {end_meeting}")
#TASK 4
# Timezone Converter
dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz = input("Enter your timezone (e.g., UTC, US/Eastern): ")
to_tz = input("Enter target timezone (e.g., Asia/Tokyo): ")
dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M')
dt_from_tz = pytz.timezone(from_tz).localize(dt)
dt_to_tz = dt_from_tz.astimezone(pytz.timezone(to_tz))
print(f"Converted time: {dt_to_tz}")
#TASK 5
# Countdown Timer
future_dt_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
future_dt = datetime.strptime(future_dt_str, '%Y-%m-%d %H:%M:%S')

while True:
    now = datetime.now()
    remaining = future_dt - now
    if remaining.total_seconds() <= 0:
        print("Countdown finished!")
        break
    print(f"Time remaining: {str(remaining).split('.')[0]}", end='\r')
    time.sleep(1)

#TASK 6
# Email Validator
email = input("Enter an email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Valid email.")
else:
    print("Invalid email.")
#TASK 7
# Phone Number Formatter
phone = input("Enter a phone number (e.g., 1234567890): ")
formatted_phone = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', phone)
print(f"Formatted phone number: {formatted_phone}")
#TASK 8
# Password Strength Checker
password = input("Enter a password: ")
strong = len(password) >= 8 and bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password)) and bool(re.search(r'\d', password))
print("Strong password." if strong else "Weak password.")
#TASK 9
# Word Finder
text = "This is a sample text for finding specific word occurrences."
word = input("Enter word to find: ")
occurrences = [m.start() for m in re.finditer(word, text)]
print(f"Occurrences of '{word}': {occurrences}")
#TASK 10
# Date Extractor
input_text = input("Enter text to extract dates: ")
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', input_text)
print(f"Extracted dates: {dates}")
