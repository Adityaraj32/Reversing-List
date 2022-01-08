'''
Author: Adityaraj Yadav 
Date: 8 January 2022
Project Name: Next Palindrome
Purpose:For Practising Purpose
'''


def comming_palindrome(n):
    if n < 10:
        n+(n-10)
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]



# First Method
number_1 = int(input("Enter The First Number: "))
add = 0
while True:
    add += 1
    number_1 += 1
    copy = copy.deepcopy(number_1)
    if number_1 < 10:
        number_1+(number_1-10)
    elif str(number_1) == str(number_1)[::-1]:
        print(f"The {copy} Next Palindrome is {add+int(copy)}")
        print(copy)
        print(number_1)
        break
    continue

# Second Method
Times = int(input("Enter how many numbers you want to show there Palindrome: "))
list = []

for i in range(Times):
    list_num = int(input("Enter the numbers: "))
    list.append(list_num)
for i in range(Times):
    print(
        f"The next palindrome for the number {list[i]} is {comming_palindrome(list[i])}")
