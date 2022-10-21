#!/bin/python3
# AgileGrabber - Multi threaded port scanner
# v1.0.1
# A project by Jay Vadhaiya
# https://github.com/sudo0x18/AgileGrabber.git
# Licensed under GNU GPLv3 Standards.  https://www.gnu.org/licenses/gpl-3.0.en.html

import os
import argparse

from modules.grabber import Grabber
from datetime import datetime

#Agile Grabber Class
class AgileGrabber:
	#Creating description and usage
	DESCRIPTION = f"""AgileGrabber is a multi threaded port scanner made with python and nmap to increase the speed of scanning."""

	USAGE = f"python3 agile_grabber.py -t TARGET -th THREADS [--help]"

	#Contructor
	def __init__(self):
		#initializing and setting argument options to be received.
		self.argParse = argparse.ArgumentParser(
			description = self.DESCRIPTION,
			usage = self.USAGE
			)
		self.argParse.add_argument("-t","--target",help="Target IP or Domain",required=True)
		self.argParse.add_argument("-th","--threads",help="Number of threads",required=True)
		self.args = self.argParse.parse_args() #parsing the arguments

	#Class method for printing banner
	@classmethod
	def show_banner(self):
		print("-"*67)
		print("""\t\t╔═╗┌─┐┬┬  ┌─┐ ╔═╗┬─┐┌─┐┌┐ ┌┐ ┌─┐┬─┐\n\t\t╠═╣│ ┬││  ├┤  ║ ╦├┬┘├─┤├┴┐├┴┐├┤ ├┬┘\n\t\t╩ ╩└─┘┴┴─┘└─┘ ╚═╝┴└─┴ ┴└─┘└─┘└─┘┴└─""")
		print("-"*67)
		print("      A multi threaded port scanner made with python and nmap")
		print("                          Version v1.0.1")
		print("           A project by Jay Vadhaiya, Github: sudo0x18")
		print("-"*67)

	#screen clearer function
	@classmethod
	def screen_clear(self):
		if os.name == "posix":
			#For linux and mac
			os.system("clear")
		else:
			#for windows
			os.system("cls")

if __name__ == "__main__":
	try:
		AgileGrabber.screen_clear()
		AgileGrabber.show_banner()
		agileGrabber = AgileGrabber()
		grabber = Grabber(agileGrabber.args.target, agileGrabber.args.threads)
		print("[+] Starting simple scan..")
		t1 = datetime.now()
		print("-"*67)
		grabber.initiate()
		grabber.q.join()
		t2 = datetime.now()
		print("-"*67)
		print(f"[*] Simple scan completed in {t2-t1} seconds")
		print("-"*67)
		print("[+] Starting advanced scan..")
		print("-"*67)
	except:
		print("\n"+"-"*67)
		print("                             Good Bye!")
		print("-"*67)