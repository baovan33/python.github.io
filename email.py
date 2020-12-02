import smtplib

#  lay thong tin 
email = "baovan.hbt.33@gmail.com"
pwd = input("Password: ")
addr = input("Sent to: ")
msg = input("Message: ")

# gui mail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try: #neu email pw dung
    server.login(email, pwd)
    print("Login succes")
    n = int(input("Time: "))
    for i in range (n): 
        server.sendmail(email, addr, msg)
    print("Message send to " + addr)
except: #neu email pw sai
    print("login error")

server.quit()

