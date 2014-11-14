#Jordan Russell
#25/10/14
#Iteration development task 1

count = 1
total = 1
n = int(input("Please input a positive number: "))
for count in range(n):
        count = count + 1
        total = total * count
print("{0}! = {1}.".format(n, total))

