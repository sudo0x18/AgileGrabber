#!/bin/python3

import threading
import os
import shutil
import socket
import concurrent.futures
import subprocess as sp

#Scanner class
class Scanner:
	#Constuctor
	def __init__(self, target, threads, open_ports):
		self.targetName = target
		self.target = socket.gethostbyname(target)
		self.threads = int(threads)
		self.open_ports = open_ports

	#Scanner function
	def scanner(self, port):
		try:
			self.nmap = "nmap -A -T4 -Pn -p{port} {target} -oN {path}".format(port=port, target=self.target, path=f"{self.targetName}/Port-{port}-scan")
			self.output = sp.getoutput(self.nmap).split("\n")
			print("\n".join(self.output[4:len(self.output)-2]))
		except:
			pass

	#Advanced Scanner function
	def advanced_scanner(self):
		try:
			if os.path.exists(self.targetName):
				shutil.rmtree(self.targetName)
			os.mkdir(self.targetName)

			with concurrent.futures.ProcessPoolExecutor() as executor:
				executor.map(self.scanner, self.open_ports)
		except:
			pass