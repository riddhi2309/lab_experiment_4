#getting the input by the user ''sentence
sentence =(input("Enter a stentence:-"))

#ititializing of the variale with zero 
i = 0
upercase = 0
lowercase = 0
digit = 0
special = 0

#starting the while loop where i is less than len(sentence)
while  i < len(sentence):
    char = sentence[i]

#starting the if condition      
    if char.isupper():
        upercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digit +=1
    else:
        special += 1
    i += 1

#printing the answers    
print("Uppercase letters:", upercase)
print("Lowercase letters:", lowercase)
print("Digits:", digit)
print("Special characters:", special)        

        