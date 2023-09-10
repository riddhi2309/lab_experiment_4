# getting the input by the user
n = int(input("Enter the number :-"))

#creating the variable staring with 0
count = 0
not_count = 0

#again we get some input by the user
number = int(input("Enter the number:-"))

#starting the while loop stating that number is not equal to '-999'
while number != -999:

#doing the if condition where we get modulus of number by n
    if number%n==0:
        count = count + 1
    else:
        not_count = not_count +1
    number = int(input("Enter the number:-"))
    
#print the anwers
print(count)
print(not_count)