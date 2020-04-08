# kwargs version:
def user_data_1(**kwargs):
    return kwargs

print(user_data_1(name='Alexei', surname='Rykov', year_of_birth='1984', city='Kemerovo', e_mail='totalkmr@mail.ru',
                tel='+79134297071'))


# f-string version:
def user_data_2(name, surname, year_of_birth, city, e_mail, tel):
    return print(f"|Имя: {name} | Фамилия: {surname} | Год рождения: {year_of_birth} | Город проживания: {city} |"
                 f" Электронная почта: {e_mail} | Телефон: {tel} |")

user_data_2(name='Alexei', surname='Rykov', year_of_birth='1984', city='Kemerovo', e_mail='totalkmr@mail.ru',
                tel='+79134297071')