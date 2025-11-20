import datetime as dt
import smtplib, random

quotes_list = []
my_email = "yburneg.business@gmail.com"
password = "uzul bvtp wybi ilpu"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("./Day 32/quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()

    random_quote = random.choice(quotes_list)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kittanjustin@yahoo.com", msg=f"Subject:A Quote for you.\n\n{random_quote}")