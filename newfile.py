import math
print("Select 1 to find factorial of a number")
print("Select 2 to find average of numbers")
print("Select 3 to find sum of numbers")
print("Select 4 to find the even numbers given in the range")
print("Select 5 to find the odd numbers given in the range")
userInput = int(input("Enter your choice"))

# 1 Factorial of a number
if userInput == 1:
    f = int(input("Enter the number to find factorial"))
    print("Factorial of ",f,"=",math.factorial(f))
    
# 2 Average of number
if userInput ==2:
    n = int(input("Enter number"))
sum = 0

# loop for average
for num in range(1, n + 1, 1):
     sum = sum + num
average = sum / n
print("Average of ", n, "numbers is: ", average)

# 3 Sum of a number
if userInput ==3:
    k = int(input("Enter number"))
sum = 0

# loop for sum
for num in range(1, k + 1, 1):
     sum = sum + num
print("Sum of first ", k, "numbers is: ", sum)

# 4 Even number
if userInput ==4:
    a = int(input("Enter the number upto which you want to print the even numbers"))
for reseven in range(0,a,2):
    print (reseven)
    
# 5 Odd number
if userInput ==5:
    b = int(input("Enter the number upto which you want to print the odd numbers"))
for resodd in range(1,a,2):
    print (resodd)