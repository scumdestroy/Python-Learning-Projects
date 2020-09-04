# INFOSEC PRO CHALLENGE 1
import re
import sys
# Can you write an if/then statement that looks for an IP and prints "Found it" if succesful? 
# Get user input, regex match it until you catch it.

print("------------------------------------")
print("-------Welcome to G.R.E.P.----------")
print("-Greatly Reduced Efficiency Program-")
print("------------------------------------")
target_ip = input("Please input the IP of your victim!\n")
print("Your victim is {}".format(target_ip))

target_file = input("Which file are you parsing?")
if re.findall(target_ip, target_file):
    print("Found it.")
    print(re.findall(target_ip, target_file))
else:
    print("I'm sorry, chief.  Not happening here.")
