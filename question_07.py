# Getting the input by the user 'x'
x = int(input("Enter the no for the fibonacci series:-"))

#stating the variable 'i','a','b','res'

i = 2
a = 1
b = 1
res = 0
#printing the first and second term of the fibonacci series

print(a,end=" ")
print(b,end=" ")
#starting the while loop
 
while i<=x:
    res = a + b
    a = b
    print(res , end=" ")
    b = res
    i += 1
