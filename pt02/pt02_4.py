my_str = input('Введите строку из нескольких слов, разделенных пробелами: ')
for word in enumerate(my_str.split(), 1):
    out_list = list(word)
    if len(out_list[1]) > 10:
        out_list[1] = out_list[1][0:10]
    else:
        pass

    print(f"{out_list[0]}. {out_list[1]}")