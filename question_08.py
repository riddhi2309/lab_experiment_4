#getting the input by the user "num"
num = int(input("enter the number:-"))

#stating the variable 'k','i'
k=0
i=2

#starting the while loop states i <num
while i<num:
    if num%i==0:
        k+=1
    i+=1

#using the if condition to state whether number is prime or not 
if k==0:
    print("it is prime")
elif num==1:
    print("it is not prime nor composite")
else:
    print("it is not prime")