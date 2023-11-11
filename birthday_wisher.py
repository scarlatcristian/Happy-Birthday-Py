import smtplib
import random
import pandas
import datetime as dt

MY_EMAIL = 'your_email_address'
MY_PASSWORD = 'your_google_apps_password'
USER_NAME = 'Anon'

now = dt.datetime.now()
current_day = dt.datetime(year=now.year, month=now.month, day=now.day)

birthdays = pandas.read_csv("./birthdays.csv").to_dict(orient='records')

for person in birthdays:
    # Check if it's person's birthday
    if person["month"] == current_day.month and person["day"] == current_day.day:

        # Open random letter and replace [NAME] and [USER_NAME]
        with open(f"./letter{random.randint(1, 3)}.txt") as letter:
            letter_content = letter.read().replace(
                '[NAME]', f"{person['name']}").replace('[USER_NAME]', USER_NAME)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"],
                                msg=f"Subject: Happy birthday!!\n\n{letter_content}")
