my_list = input('Введите элементы списка через пробел: ').split()

i = 0
for n in range(len(my_list) // 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print(my_list)