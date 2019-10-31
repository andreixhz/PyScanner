import socket,sys
import pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)
begin = datetime.now()

def choose_scan():
    topports = [20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    print("\nChoose a type of scan: ")
    print("1 - Top 20 ports")
    print("2 - All ports (1 to 65535)")
    selected = input(">>")

    number_choosed = []

    if (selected == '1'):
        number_choosed = topports
        return number_choosed
    elif (selected == '2'):
        allports_scan()  
    else:
        print("Invalid option!")

def port_scan():
    ip = input("Type the ip address:")
    port_list = choose_scan()
    print("Scanning {} for open ports".format(ip))
    for port in port_list:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(0.5)
        if (mysocket.connect_ex((ip,port)) == 0):
            print("[*] Open TCP port:", port)
            mysocket.close()

def allports_scan():
    ip = input("Re-Type the ip address:")
    print("Scanning {} for open ports".format(ip))
    for port in range(1,65535):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(0.5)
        if (mysocket.connect_ex((ip,port)) == 0):
            print("[*] Open TCP port:", port)
            mysocket.close()

port_scan()

final = datetime.now()
total_time = (final - begin)
print("\nScript Duration:", total_time)
print("Written by: grmelito") 

			    
