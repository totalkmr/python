class CheckList(Exception):
    def __init__(self):
        self.my_list = []

    def check_add(self):
        while True:
            try:
                inp_user = input('Для выхода введите "stop".\n'
                                 'Введите элемент списка: ')
                if inp_user == 'stop':
                    print(f'Итоговый список: {self.my_list}.\n'
                          f'*** Работа программы завершена. ***')
                    break
                else:
                    self.my_list.append(int(inp_user))
                    print(f'Текущий список: {self.my_list}.\n')
            except:
                print('Введен некорректный тип данных (str или bool)!\n')


a = CheckList()
a.check_add()