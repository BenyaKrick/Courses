"""
[2] Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет),
type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение
«Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение
автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.
"""


class Car:
    color = None
    typecar = None
    year = None

    def __init__(self, color, typecar, year):
        self.color = color
        self.typecar = typecar
        self.year = year

    def EngineON(self):
        print('Engine ON')

    def EngineOFF(self):
        print('EngineOFF')

    def CarYear(self, getyear):
        self.getyear = getyear

    def CarType(self, gettype):
        self.gettype = gettype

    def CarColor(self, getcolor):
        self.getcolor = getcolor

car = Car('red', 'sedan', '2017')
print(car.__dict__)
car.EngineON()
car.EngineOFF()

car.CarYear(2002)
car.CarColor('blue')
car.CarType('Coupe')
print(car.__dict__)
