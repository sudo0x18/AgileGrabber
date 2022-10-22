#!/bin/python3

import threading
import os
import shutil
import socket

#Scanner class
class Scanner:
	#Constuctor
	def __init__(self, target, threads, open_ports):
		self.target = socket.gethostbyname(target)
		self.threads = int(threads)
		self.open_ports = open_ports

	#Advance Scanner function
	def advanced_scanner(self):
		try:
			self.nmap = "nmap -A -T4 -Pn -p{port} {target} -oN {path}".format(port=",".join(self.open_ports), target=self.target, path=f"{self.target}/advanced")
			print(f"Scan Command: {self.nmap}")
			print("-"*67)
			if os.path.exists(self.target):
				shutil.rmtree(self.target)
			os.mkdir(self.target)
			os.system(self.nmap)
		except Exception as e:
			pass
