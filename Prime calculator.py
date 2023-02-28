from math import ceil
n = int(input("Enter a posotive integer to test: "))
flag = False

i = 2
while i <= ceil(n/2) and flag == False:
    if n/i == int(n/i):
        print(str(n)+" is composite")
        flag = True
    i = i+1
if flag == False:
    print(str(n)+" is prime")
