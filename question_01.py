# getting the input by the user 
n = int(input("Enter the value for n:-"))

#starting the value with the 1 
count = 1

# to display the invalid case
if n <0 or n==0:
    print("Invalid case")

# using the while loop to display the result
while count<21:
    
# define variable table to multiply the count and n
    table = count*n   
    print(n,"X",count , " = ", table)
    count += 1