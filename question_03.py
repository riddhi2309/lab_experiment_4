#getting the input by the user "n"
n = int(input("Enter the digit:- "))

#defing a variable which starts with 0 
addition = 0
 
#starting the while loop stating  n is not equal to 0
while n != 0:
    addition = addition+(n%10)
    n = n//10
print(addition)