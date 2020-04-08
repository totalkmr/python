time_sec = int(input('Введите время в секундах: '))

hour = time_sec // 3600
minute = (time_sec // 60) % 60
second = time_sec % 60

print(f"Время: {hour}:{minute}:{second}")