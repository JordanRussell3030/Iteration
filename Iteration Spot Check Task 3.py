#Jordan Russell
#11/11/14
#Iteration Spot Check Task 3

import random
guessed = False
number = random.randint(1, 100)
number_of_turns = 0
while guessed == False:
    number_of_turns = number_of_turns + 1
    user_guess = int(input("Please enter your guess for the number: "))
    if user_guess == number:
        guessed = True
    elif user_guess > number:
        print("The number you guessed is too high.")
    elif user_guess < number:
        print("The number you guessed is too low.")
    if guessed == True:
        print("You took {0} turns to guess the number.".format(number_of_turns))
        print("The number was: {0}.".format(number))
        
        
