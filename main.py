import csv
import datetime as dt
import csv
import random
import os
import smtplib
birthday_list={}
now=dt.datetime.now()
month=now.month
day=now.day
annual_day=(f"{month},{day}")


def send_email():
    folder_path = "./letter_templates"
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    random_file = random.choice(text_files)
    full_file_path = os.path.join(folder_path, random_file)
    with open(full_file_path, mode="r", encoding="utf-8") as file:
        file_contents = file.read()
        updated_contents = file_contents.replace("[NAME]", row['name'])
        msg_body = updated_contents
        msg_body = (f"Subject: HAPPY BIRTHDAY\n\n{updated_contents}")
        print(msg_body)
    my_email = "p61668338@gmail.com"
    password = "cskr nnag azkb kgoh"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
         connection.starttls()
         connection.login(user=my_email, password=password)
         connection.sendmail(from_addr=my_email,
                              to_addrs="p61668338@gmail.com",
                              msg= msg_body)

with open ("birthdays.csv",mode="r") as file:
    reader = csv.DictReader(file)
    birthday_list=list(reader)
    for row in birthday_list:
        if int(row['month']) == month  and int(row['day']) == day:
           send_email()






