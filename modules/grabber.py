#!/bin/python3

import socket
import threading
import queue
import os
import shutil

#Grabber class
class Grabber:
	#Constuctor
	def __init__(self, target, threads):
		self.target = socket.gethostbyname(target)
		self.threads = int(threads)
		self.q = queue.Queue()
		self.print_lock = threading.Lock()
		self.open_ports = []
		socket.setdefaulttimeout(2)

	#Scanner Function
	def scanner(self, port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.conn = self.client.connect((self.target, port))
			with self.print_lock:
				print(f"{port} is open")
				self.open_ports.append(str(port))
			self.client.close()
		except Exception as e:
			pass

	#Threader class
	def threader(self):
		while True:
			self.p = self.q.get()
			self.scanner(self.p)
			self.q.task_done()

	#Initiate function
	def initiate(self):
		for i in range(self.threads):
			self.thread = threading.Thread(target=self.threader, daemon=True)
			self.thread.start()

		for port in range(1, 65536):
			self.q.put(port)

	#Advance scan function
	def advance_scan(self):
		try:
			self.nmap = "nmap -A -T4 -Pn -p{ports} {target} -oN {path}".format(ports=",".join(self.open_ports), target=self.target, path=f"{self.target}/advancedScan")
			print("Scan Command: " + self.nmap)
			if os.path.exists(self.target):
				shutil.rmtree(self.target)
			os.mkdir(self.target)
			os.system(self.nmap)
		except Exception as e:
			print(e)