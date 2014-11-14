#Jordan Russell
#21/10/14
#Iteration development task 2

stars_per_row = int(input("Please input how many stars you would like in your row: "))
number_of_rows = int(input("Please input how many rows of stars you would like: "))
star = "*" * stars_per_row
for stars in range(number_of_columns):
    print(star[0:stars_per_row])
    
