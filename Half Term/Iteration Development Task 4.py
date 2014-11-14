#Jordan Russell
#28/10/14
#Iteration Development Task 4

invalid = True
largest_number = 0
number = 0
count = 1
print("This program will find the largest number from a series of numbers. Please input -1 to finish entering numbers.")
while invalid:
    number = int(input("Please enter number {0}: ".format(count)))
    count = count + 1
    if largest_number == 0:
        largest_number = number
    elif largest_number < number:
        largest_number = number
    elif number == -1:
        print("The largest number you have enterd is {0}.".format(largest_number))
        invalid = False
