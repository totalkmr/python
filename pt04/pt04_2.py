my_list = [2, 4, 5, 2, 1, 5, 6, 7, 3, 3, 2]

new_list = [my_list[i] for i in range(1, len(my_list)) if int(my_list[i]) > int(my_list[i - 1])]

print (new_list)