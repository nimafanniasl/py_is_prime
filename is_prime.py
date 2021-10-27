#smartnima - Nima Fanniasl

import math
from time import sleep
from yrange.yrange import yrange  #https://github.com/nimafanniasl/py_yrange (pip install yrange)

def is_prime(num):
    if num == 1:
        return False
    Is_prime = True

    
    for i in yrange(int(math.sqrt(num))+1,2):
        if num % i != 0:
            Is_prime = True
        elif num % i == 0:
            return False
    return Is_prime
def rangenum():
    start = int(input("enter start number: "))
    end = int(input("enter end number: ")) + 1
    #prime = list()
    #not_prime = list()
    print("prime:")
    for i in yrange(end,start):
        if is_prime(i):
            sleep(0.5)
            print(i,end=" , ")
    print("Not prime:",end=" ")
    for i in yrange(end,start):
        if not is_prime(i):
            sleep(0.5)
            print(i)
    #for i in list(range(len(prime))):
    #    if i == len(prime) - 1:
    #        print(prime[i],end="")
    #    else:
    #        print(prime[i],end=" , ")
    #print()
    #print("not prime:",end=" ")
    #for i in list(range(len(not_prime))):
    #    if i == len(not_prime) - 1:
    #        print(not_prime[i],end="")
    #    else:
    #        print(not_prime[i],end=" , ")
def one_number():
    num = int(input("enter number: "))
    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")
def start():
    tmp = input('''Do you want to give the program a numeric range or one number? (for help type help) :  ''')
    if tmp == "range":
        rangenum()
    elif tmp == "one number":
        one_number()
    elif tmp == "help":
        print("Enter the word range for range and the word one number for a number.")
        start()
    else:
        print("Error")
        start()
####################################
start() # start the program
print()
input("enter any key to continue...")
