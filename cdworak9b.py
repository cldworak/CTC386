Lab 9 
#Cherie Dworak 
#upload to github 


#This is the function definitions 
def celtofah_function (celsius0:
    celsius = (f-32) * 5/9
    return celsius


name = input ("What is your name?")

print ( name, "Let's play! Pick an option.")

print ("     Menu     ") 
print ("_________________________________")
print ("Option 1")
print ("Option 2")
print ("Option 3") 
print ("Option 4")
print ("Option 5") 

print ("Hello", name, "Enter an option")
 
#This is the main section
option = input()


if option == "1": 
    for i in range(1):
        print ("What do you call a cheese that is not yours? NACHO cheese!")

elif option == "2": 
    for i in range (15): 
        print (name, ) 

elif option == "3": 
    guess = int (input ("Enter a number: "))
    for i in range (guess): 
        print ( "You're killin' me, smalls!" ) 

elif option == "4": 

    print  ("Guess my number! Are you ready?")
    guess = int (input ("Enter a number"))  
    while (guess != 67): 
    
        #range for guess 
        while (guess < 0) or (guess > 100):
            guess = int(input ("Enter your guess between 1 and 100:")) 
            if (guess < 0) or (guess > 100):
                print ("Your guess is out of range") 

        if (guess > 67): 
            print ("your guess is too high")
            guess = int (input ("Try again"))
        elif (guess < 67): 
            print ("your guess is too low") 
            guess = int (input ("Try again")) 
        else: (guess == 67) 
        print ("Congrats! you guessed my number, 67") 

elif option == "5": 

        f= float(input("Enter the temp. in Fahrenheit."))

        output = celtofah_function (f)

        print ("The temp in celsius is", output)
