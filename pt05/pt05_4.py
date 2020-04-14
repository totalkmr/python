dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
list_out = []
with open('pt05_4_in.txt', encoding='utf8') as f_in:
    for num_name in f_in:
        num_name = num_name.split(' - ')
        list_out.append(dict_num[num_name[0]] + ' - ' + num_name[1])
with open('pt05_4_out.txt', 'w') as f_out:
    f_out.writelines(list_out)