import socket,sys
from datetime import datetime

begin = datetime.now()

topports = [20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]

ip = input("Type the ip address:")

def choose_scan():
    print("\nChoose a type of scan: ")
    print("1 - Top 20 ports")
    print("2 - All ports (1 to 65535)")
    print("3 - Uniq port")
    selected = input(">>")

    number_choosed = []

    if (selected == '1'):
        port_scan()
    elif (selected == '2'):
        allports_scan()
    elif (selected == '3'):
        unique_port()
    else:
        print("Invalid option!")

def port_scan():
    print("Scanning {} for open ports".format(ip))
    for port in topports:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(0.5)
        if (mysocket.connect_ex((ip,port)) == 0):
            print("[*] Open TCP port:", port)
            mysocket.close()

def allports_scan():
    print("Scanning {} for open ports".format(ip))
    for port in range(1,65535):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(0.5)
        if (mysocket.connect_ex((ip,port)) == 0):
            print("[*] Open TCP port:", port)
            mysocket.close()

def unique_port():
    port = int(input("Type the port:"))
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(0.5)
    if (mysocket.connect_ex((ip,port)) == 0):
        print("[*] Open TCP port:", port)
        mysocket.close()

choose_scan()

final = datetime.now()
total_time = (final - begin)
print("\nScript Duration:", total_time)
print("Written by: grmelito") 