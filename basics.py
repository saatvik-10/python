# import random
from random import *
import sys

print("What is your name?")
myName = input()
print("It is nice to meet you, {}" .format(myName))

print("-----------------------------------------------------------------------------------------------------")

while True:
    print("Who are you?")
    name = input()

    if name != "Saatvik":
        continue

    print("Hello Saatvik...what is your password?")
    password = input()

    if password == "messi":
        break

print("Access Granted")

print("-----------------------------------------------------------------------------------------------------")

print("The GOAT is")

for i in range(5):
    print("MESSI, {}" .format(str(i)))
    
print("-----------------------------------------------------------------------------------------------------")

for i in range(0, 10, 2):
    print(i)
    
for i in range(10, -4, -2):
    print(i)
    
print("-----------------------------------------------------------------------------------------------------")

for i in range(5):
    print(randint(1, 10))
    
print("-----------------------------------------------------------------------------------------------------")

while True:
    print("Type exit to exit")
    res = input()
    
    if res == 'exit':
        sys.exit()
        
    print("You typed {}" .format(res))
