#getting the by the user 'n'
n = int(input("Enter your number:-"))

#stating the variable factorail starting with 1
factorial = 1

#starting the while loop where n>0
while n >0:
    factorial = factorial*n
    n=n-1

#printing the answer using the 'f' function   
print(f"The factorial of this number is {factorial}")