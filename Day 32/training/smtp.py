import smtplib

my_email = "yburneg.business@gmail.com"
password = "uzul bvtp wybi ilpu"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="kittanjustin@yahoo.com", msg="Subject:Hello\n\nThis is the new body of my email.")
#connection.close() ---> when using the "with" key word, you don't need this line of code any more