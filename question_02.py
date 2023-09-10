# getting the number x,y,z by the user 
x= int(input("Enter the number:-"))
Y= int(input("Enter the number:-"))
N= int(input("Enter the number:-"))

#using the while loof to find the number
while x<Y:
    x= x+1
    if x%N==0:
        print(x)
