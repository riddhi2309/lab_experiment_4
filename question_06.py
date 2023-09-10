#Getting the input from thr user 'num'
num = int(input("Enter the number:-"))

#stating the variable 
a=num
b=0

#starting the while loop
while num>0:
    c = num%10
    b = b*10 + c
    num = num//10
if a==b:
    print("The number is palindrome")
else:
    print("The number is not palindrome")