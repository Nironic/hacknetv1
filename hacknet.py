#modules
import socket
import os
import subprocess
import sys
import time
#banner
print('██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗' )
print(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝')
print(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║'   )
print(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║'   )
print(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║'	 )
print(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝'	 )
#main-menu
def main():
#a lot of print's :)
	print("|Thank|", end = "")
	time.sleep(0.1)
	print("|You|", end = "")
	time.sleep(0.4)
	print("|For|", end = "")
	time.sleep(0.7)
	print("|Using|", end = "")
	time.sleep(0.10)
	print("|My|", end = "")
	time.sleep(0.11)
	print('|Script|')
	
	print("""
         ______________________________________________
	|Author:Reffy|My VK:https://vk.com/mrgurutopyt |
	|My GitHub:https://github.com/reffyMelon       |
	|The creation date of the script:22.04.2019    |
	 ______________________________________________ 
    ____________________
  +|Developed for Termux|+
 ==========================
    """)
#Device information 
print('Name of your OS...')
os.system('uname -o')
print('Other system info...')
if os.system("neofetch") == 1:
 os.system('pkg install neofetch')
print('Menu:')
print('$##########################$')
print('1)Gratitudes')
print('2)Nmap')
print('3)Metasploit')
print('Port scan')
print('Whois')
print('IP Lookup')
main()

