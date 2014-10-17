#Jordan Russell
#17/10/14
#Iteration revision task 5

total_numbers = 0
number = 0
loop_count = 0
print("Please input a series of numbers, and enter -1 to finish. ")
while number >= 0:
    number = int(input("Please enter a number: "))
    if number >= 0:
        total_numbers = total_numbers + number
        loop_count = loop_count + 1
print(total_numbers / loop_count)


   
    
 
