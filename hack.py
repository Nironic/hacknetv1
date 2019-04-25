# -*- coding: utf-8 -*-
#modules
import os # Use
import subprocess # Use
import sys # Use
import time # Use
try:
	import colorama
except:
	print("Install colorama")
	os.system("pip install colorama")

try:
	from termcolor import colored
except:
		print("Install termcolor")
		os.system("pip install termcolor")

os.system("clear")
"""
Tool:

The tool is created exclusively for the program Thermex on Android.
----------------------------------------------------------------------------------------
Packages are installed via pkg.
----------------------------------------------------------------------------------------
Packages will be configured depending on what button you press.
If you have root permissions you are allowed more. 
The package will be updated within a month.
----------------------------------------------------------------------------------------
Tools that can be installed through this package:
----------------------------------------------------------------------------------------
Metasploit Framework,
Nmap,
Neotech,
Check open ports. //This can also be done via nmap in more detail.
----------------------------------------------------------------------------------------
Thank you for using our package to install other utilities on Thermex.
"""

def banner():
	print(colored(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗', "red"))
	print(colored(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝', "blue"))
	print(colored(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║', "red"))
	print(colored(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║', "blue"))
	print(colored(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║', "red"))
	print(colored(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝', "blue"))
	#print("User:", str(os.environ.get("USERNAME"), "loading conf.")
	print(colored("""
	 ______________________________________________ 
	 |Author:Reffy|My VK:https://vk.com/mrgurutopyt |
	 |My GitHub:https://github.com/reffyMelon       |
	 |The creation date of the script:22.04.2019    |
	  ______________________________________________
	  ########################
	  # Developed for Termux #
	  ########################
	""", "green"))

#main-menu
def main():
		#Device information	
		banner()
		print('Name of your OS...')
		os.system('uname -o') # Os command line
		print(colored('Other system info...', "red"))
		os.system("neofetch")
		print(colored('Menu:', "blue"))
		print('$##########################$')
		print(colored('1)Gratitudes', "yellow"))
		print(colored('2)Nmap', "red"))
		print(colored('3)Metasploit', "red"))
		print(colored('4)Port scan', "yellow"))
		print(colored('5)Whois', "green"))
		print(colored('6)IP Lookup', "red"))
		print(colored('7)Quit', "blue"))
		print('----------------------------')
		join()


def menu():
	os.system("clear")
	main()

"""
Execute neofech: 

..............                                     root@kali 
            ..,;:ccc,.                             --------- 
          ......''';lxO.                           OS: Kali GNU/Linux Rolling  
.....''''..........,:ld;                           Host: HP Laptop 15-bs1xx 
           .';;;:::;,,.x,                          Kernel: 4.19.0-kali3-686-pa 
      ..'''.            0Xxoc:,.  ...              Uptime: 1 hour, 58 mins 
  ....                ,ONkc;,;cokOdc',.            Packages: 3033 (dpkg) 
 .                   OMo           ':ddo.          Shell: bash 5.0.3 
                    dMc               :OO;         Resolution: 1366x768 
                    0M.                 .:o.       DE: GNOME 3.30.1 
                    ;Wd                            WM: GNOME Shell 
                     ;XO,                          WM Theme: Kali-X 
                       ,d0Odlc;,..                 Theme: Kali-X [GTK2/3] 
                           ..',;:cdOOd::,.         Icons: Vibrancy-Kali [GTK2/ 
                                    .:d;.':;.      Terminal: gnome-terminal 
                                       'd,  .'     CPU: Intel i3-5005U (4) @ 1 
                                         ;l   ..   GPU: Intel HD Graphics 5500 
                                          .o       Memory: 1751MiB / 3886MiB 
                                            c
                                            .'                             
                                             .


"""
def join():
	while True:
		temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		hpt = input(temp)


		if hpt == "1":
				print("""
													
				############################################## =========
				#Second developer:https://github.com/inkviz96# Writes port-scanner         
				############################################## =========
				""")


		if hpt == "2":
			print('install Nmap') #print
			os.system("apt update && apt upgrade") #Update apt and System termux
			os.system("pkg install nmap") #Install nmap
			print("The installation is finished")


		if hpt == "3":
			print('install Metasploit')
			os.system("apt update && apt upgrade") #Update apt and System termux
			os.system("pkg install unstable-repo") #Install repositories
			os.system("pkg install metasploit") #Install metasploit


		if hpt == "7":
			print("Goodbay")
			exit()



#Start old process for programm
menu()