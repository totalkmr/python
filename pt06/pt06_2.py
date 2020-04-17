class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def asphalt_mass(self):
        weight = 50
        thickness = 0.01
        return self._lenght * self._width * weight * thickness


road_first_category = Road(500, 375)
print(f'Для строительства дорожного полотна c заданными параметрами необходимо {road_first_category.asphalt_mass()} '
      f'кг асфальта.')