#An-IP-Address-Information-Gathering-Tool
#Coded by:fbitactical on Instagram.

import requests
import sys

print()
print("▄▄▄█████▓ ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▄████▄   ▄▄▄       ██▓ ")   
print("▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒ ")   
print("▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░ ")   
print("░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░   ") 
print("  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒ ")
print("  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░ ")
print("    ░      ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░ ")
print("  ░        ░   ▒   ░          ░       ▒ ░░          ░   ▒     ░ ░    ")
print("               ░  ░░ ░                ░  ░ ░            ░  ░    ░  ░ ")
print("                   ░                     ░                           ")
print()
print("          [+] Coded-by: instagram.com/fbitactical/ [+]               ")

ip_address = input("Enter an ip-address: ")
response = requests.get("http://ip-api.com/json/" + ip_address)

print(response.json())
