#getting the input from he user 'a','b','c'
a = int(input("Enter the cofficent of x^2:-"))
b = int(input("Enter the cofficent of x:-"))
c = int(input("Enter the number:-"))

#finding the diterminant of the roots
d =((b**2) - (4*a*c))

#formula to find the roots of the quadratic 
root1 = ((-b) + (d**0.5))/(2*a) 
root2 = ((-b) - (d**0.5))/(2*a) 
root3=((-b)/(2*a))

#using the if function to determine the nature of the root
if d <0:
    print ("The roots are imaginary")
elif d==0:
    print(root3)
else:
    print(root1, root2 ,"The roots of the quadratic equation are real")  
