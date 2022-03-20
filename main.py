from datetime import datetime
import random
import pandas
import smtplib

MY_EMAIL = "pythonproject862@gmail.com"
MY_PASSWORD = "goober1!"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
birthday_person = birthday_dict[today_tuple]

if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"].title())

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")
