import random

print("Enter name to greet")
name = input()

def hello(name):
    print("Hello {}" .format(name))
    
hello(name)

print("-----------------------------------------------------------------------------------------------------")

def getAns(ans):
    if ans == 1:
        return "You got it"
    elif ans == 2:
        return "Try again"
    elif ans == 3:
        return "Still no, try again"
    
r = random.randint(1, 3)
print(r)

luck = getAns(r)
print(luck)

print("-----------------------------------------------------------------------------------------------------")

def spam():
    global eggs
    eggs = 'spammer'
    
eggs = 'spamming'
spam()

print(eggs)

print("-----------------------------------------------------------------------------------------------------")

def spam(divisionBy):
    try:
        return 42 / divisionBy
    
    except ZeroDivisionError as err:
        print("Err: Invalid Input: {}" .format(err))
        
    finally:
        print("EXECUTION FINISHED!")
        
print(spam(21))
print(spam(2))
print(spam(5))
print(spam(0))