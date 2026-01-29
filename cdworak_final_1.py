#CTC386 Final_1 
#Cherie Dworak 


name = input ("What is your name?")

print ( name, "Let's play! Pick an option.")

print ("     Menu     ") 
print ("_________________________________")
print ("Option 1")
print ("Option 2")
print ("Option 3")  

print ("Hello", name, "Enter an option")
 

option = input()


if option == "1": 
    for i in range(1):
        print (name, "What do you call a cheese that is not yours? NACHO cheese!")

elif option == "2": 
    for i in range (20): 
        print ("Nacho Cheese") 

elif option == "3":    
    guess = 1     
    while (guess != 0): 
        guess = int(input ("Enter a number"))

        if (guess != 0):
            print("Warning! try again") 

    print ("Congrats! you guessed my number, 0") 

