#Jordan Russell
#1/11/14
#Iteration Stretch and Challenge Task 4

word_count = 0
found = False
list_of_items = ""
list_of_items = input("Please input a phrase: ")
length_of_list = len(list_of_items)
while (found == False) and (word_count == max):
    if length_of_list == list_of_items[0]:
        found = True
        print(length_of_list)
    else:
        word_count = word_count + 1
print(length_of_list)
