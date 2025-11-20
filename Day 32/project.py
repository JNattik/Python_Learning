import smtplib, random, pandas
import datetime as dt

date_1 = dt.datetime.now()
month = date_1.month
day = date_1.day
my_email = "yburneg.business@gmail.com"
password = "uzul bvtp wybi ilpu"

birthdays = pandas.read_csv("./Day 32/birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

for x in birthdays_dict:
    if x["day"] == day and x["month"] == month:
        file_path = f"./Day 32/letter_{random.randint(1,2)}.txt"
        with open(file_path) as letter_files:
            contents = letter_files.read()
            new_contents = contents.replace("[NAME]", x["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=x["email"], msg=f"Subject:Birthday wishes.\n\n{new_contents}")