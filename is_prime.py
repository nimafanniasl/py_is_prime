#smartnima - Nima Fanniasl
import math

def is_prime(num):
    if num == 1:
        return False
    Is_prime = True

    
    numlist = list(range(2,int(math.sqrt(num))+1))
    for i in numlist:
        if num % i != 0:
            Is_prime = True
        elif num % i == 0:
            return False
    return Is_prime
def rangenum():
    start = int(input("enter start number: "))
    end = int(input("enter end number: ")) + 1
    numbers = list(range(start,end))
    prime = list()
    not_prime = list()
    for i in numbers:
        if is_prime(i):
            prime.append(i)
        else:
            not_prime.append(i)
    print("prime:",end=" ")
    for i in list(range(len(prime))):
        if i == len(prime) - 1:
            print(prime[i],end="")
        else:
            print(prime[i],end=" , ")
    print()
    print("not prime:",end=" ")
    for i in list(range(len(not_prime))):
        if i == len(not_prime) - 1:
            print(not_prime[i],end="")
        else:
            print(not_prime[i],end=" , ")
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