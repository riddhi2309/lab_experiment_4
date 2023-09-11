#getting the input by the user 'char'
char = input("Enter the string : ")
#creating the list 'up','low','digit','specase'
up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit = ["0",'1','2','3','4','5','6','7','8','9']
specase=["!","@","#","$","%",'^','&',"*","/","?","~"]
#intializing the variable
up_i = 0
low_i = 0
digit_i = 0
specase_i = 0
#creating the new variable to count the length of the char 
length=len(char)
i=0
#starting the while loop by stating the 
while i<length:
    if char[i] in up:
        up_i=up_i+1
    elif char[i] in low:
        low_i=low_i+1
    elif char[i] in digit:
        digit_i=digit_i+1
    else:
        specase_i=specase_i+1
    i=i+1       
#printing the result
print("UPPERCASE",up_i)
print("lowercase",low_i)
print("Digits",digit_i)
print("Special Characters",specase_i)        

        
