#!/usr/bin/env python3

import socket
import sys

def banner():
       print("""
 -------------------- 
   Imperial March 
   of Scanning Ports
 -------------------- 
    \   
     \
                ________
           _..-Y  |  |  Y-._
       .-~`   ||  |  |  |   `-.
       I`  ``==´|` !`´! ´|´[]´´| 
       _____SCANNING PORTS.....___________
       L__  [] |..------|:    _[----I`` .-{´-.
      I___|  ..| l______|l_  [__L]_[I_// r(=}=-P
     [L______L_[________]______j-  `-=c_]// -^
      \I_j.--.\=I|I==_/ --L_]
        [_((==) '-----' (==)j
           I--I'--   --'I--I
           |[]|         |[]|
           l__j         l__j
           |!!|         |!!|
           |..|         |..|
           ([])         ([])
           ]--[         ]--[
           [_L]         [_L]  
          / .. /       / .. /
         `=}--{=`     `=}--{=´
        .-^--r-^-.   .-^--r-^-.

""")

def scan():
       ports = [21,22,23,25,53,80,88,110,111,119,135,137,138,139,143,156,161,389,443,445,465,512,513,631,993,995,1723,2222,3306,3389,5900,8080]

       print("Port          Service        State\n\n")
       for port in ports:
              client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              resp = client.connect_ex((target,port))
              
              if(resp == 0):
                     print(f"{port}              {socket.getservbyport(port)}           OPEN\n")
              else:
                     print(f"{port}              {socket.getservbyport(port)}           closed\n")

       client.close()

try:  
        target = sys.argv[1]
        if(sys.argv == 1):
            print("Usage: python3 scan.py [TARGET IP]")
        else:
            banner()
            scan()

except KeyboardInterrupt:
       print("Exiting...")
       quit()
except socket.gaierror:
        print("Host not found...")