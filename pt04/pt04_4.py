my_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]

new_list = [el for el in my_list if my_list.count(el) == 1]

print(new_list)