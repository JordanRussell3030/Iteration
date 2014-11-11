#Jordan Russell
#11/11/14
#Iteration Spot Check Task 2

count = 0
times_table = int(input("Please enter an integer: "))
print("Times table for {0}:".format(times_table))
for count in range(12):
    count = count + 1
    print("{0:.>} * {1} = {2}".format(count, times_table, count * times_table))
    
