# -*- coding: utf-8 -*-
#modules
import socket # Not use
import os # Use
import subprocess # Use
import sys # Use
import time # Use
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
	print(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗' )
	print(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝')
	print(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║'   )
	print(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║'   )
	print(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║'	 )
	print(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝'	 )
	print("""
	  ______________________________________________ 
	 |Author:Reffy|My VK:https://vk.com/mrgurutopyt |
	 |My GitHub:https://github.com/reffyMelon       |
	 |The creation date of the script:22.04.2019    |
	  ______________________________________________
	  ########################
	  # Developed for Termux #
	  ########################
	""")  

#main-menu
def main():
	#a lot of print's :)
	banner() # Loading banner
	time.sleep(0.1) # sleep
	print("you", end = "")
	time.sleep(0.4) # sleep
	print("for", end = "")
	time.sleep(0.7) # sleep
	print("using", end = "")
	time.sleep(0.10) # sleep
	print("my", end = "")
	time.sleep(0.11) # Sleep 0.11 min.sec
	print('script')
	#Device information	
	print('Name of your OS...')
	os.system('uname -o') # Os command line
	print('Other system info...')
	if os.system("neofetch") == 1:
		os.system('pkg install neofetch') #Install neofetch execute:




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




print('Menu:')
print('$##########################$')
print('1)Gratitudes')
print('2)Nmap')
print('3)Metasploit')
print('4)Port scan')
print('5)Whois')
print('6)IP Lookup')
print('7)Quit')
hpt = input("[$hpt]>")



def restart():
	#copied from https://github.com/Gameye98/Lazymux
	python = sys.executable # ne ebu)))
	os.execl(python, python, * sys.argv) # Ne ebu
	curdir = os.getcwd() # dir os



def back():
	##copied from https://github.com/Gameye98/Lazymux
	print('Quit!')
	back = input("[$hpt]>")
	if back == "7":
		restart()
	else:
		print('ERROR!')
		time.sleep(2) # Sleep 2 sec
		restart() # Restart to programm


	if hpt == "1":
		print("""
								       
		############################################## =========
		#Second developer:https://github.com/inkviz96# Writes port-scanner         
		############################################## =========
		""")
Nmap = input("[$hpt]>")


if hpt == "2":
	print('install Nmap') #print
	subprocess.run("apt update && apt upgarde") #Update apt and System termux
	subprocess.run("pkg install nmap") #Install nmap
	print("The installation is finished")


Metasploit = input("[$hpt]>")


if hpt == "3":
	print('install Metasploit')
	subprocess.run("apt update && apt upgrade") #Update apt and System termux
	subprocess.run("pkg install unstable-repo") #Install repositories
	subprocess.run("pkg install metasploit") #Install metasploit


Quit = input("[$hpt]>")


if hpt == "7":
	print("Quit back to menu")
	back() # back to menu
else:
	print('ERROR!')
	time.sleep(2) #Sleep for 2 sec
	restart() #restart programm



#Start old process for programm
main()

