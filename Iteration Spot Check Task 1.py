#Jordan Russell
#11/11/14
#Iteration Spot Check Task 1 Part d

number = 0
total = 0
while number != -1:
    number = int(input("Please enter a number: "))
    if number != -1:
        total = total + (number * number)
print("The total is {0}.".format(total))
