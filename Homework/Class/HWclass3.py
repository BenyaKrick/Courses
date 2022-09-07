"""
[2] Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет),
type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение
«Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение
автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.
"""


class Car:

    def __init__(self, color, cartype, year):
        self.color = color
        self.cartype = cartype
        self.year = year

    def Engine_on(self):
        print('Engine ON')

    def Engine_off(self):
        print('EngineOFF')

    def Car_year(self, year):
        self.year = year

    def Car_type(self, cartype):
        self.cartype = cartype

    def Car_color(self, color):
        self.color = color

car = Car('red', 'sedan', '2017')
print(car.__dict__)
car.Engine_on()
car.Engine_off()

car.Car_year(2002)
car.Car_color('blue')
car.Car_type('Coupe')
print(car.__dict__)
