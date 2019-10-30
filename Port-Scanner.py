import socket,sys
from datetime import datetime

begin = datetime.now()
ip = input("Type the ip address:")

print("Scanning {} for open ports".format(ip))
for port in range(1,100):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(0.5)
    if (mysocket.connect_ex((ip,port)) == 0):
        print("[*] Open TCP port:", port)
        mysocket.close()

final = datetime.now()
total_time = (final - begin)
print("\nScan Duration:", total_time)
print("Written by: grmelito") 


	

		       

