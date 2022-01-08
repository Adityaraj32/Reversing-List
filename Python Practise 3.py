'''
Author: Adityaraj Yadav 
Date: 8 January 2022
Project Name: Reversing a list 
Purpose: For Practising Purpose
'''

# Reversing a String

# Taking Input for the list
# this is a mannual type list you can also use it
# list1 = [1,50,100,500].


Times = int(input("Enter how many numbers should be in the list: "))
list1 = []
for i in range(Times):
    list1.append(int(input("Enter the numbers: ")))
print(f"Your list is {list1}")


# using Slicing
reverse = list1[::-1]
print(f"The Reversed list of {list1}is{reverse}\n")

# Using Built In Method
reverse2 = list1[:]
reverse2.reverse()
print(f"The Reversed list of {list1}is{reverse2}")

# using replacing the first letter and second letter for first and so on
reverse3 = list1[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3)-i -
                          1] = reverse3[len(reverse3)-i-1], reverse3[i]
print(f"The Reversed list of {list1}is{reverse3}")

if reverse == reverse2 and reverse2 == reverse3:
    print("All the methods give the same results")
else:
    print("There is a mistake in doing the methods")
