my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент списка (число от 0 до 9): '))
print('Исходный список: ', my_list)
my_list.append(new_el)
sort_list = sorted(my_list)

print(f"Пользователь ввел новый элемент списка: {new_el}. Результат: {sort_list[::-1]}")