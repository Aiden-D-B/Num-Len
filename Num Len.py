number = (input("Enter a 3 digit number\n")) 
numlen = len(number) 
if numlen ==3: 
    print(str(number)+" is a 3 digit number!") 
elif numlen >3: 
    print("This number is not 3 digits long!") 
elif numlen <3: 
    print("This number is not 3 digits long!")
