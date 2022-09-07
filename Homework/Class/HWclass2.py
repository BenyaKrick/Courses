"""
[1] Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение,
multiplication — умножение, division — деление, subtraction — вычитание. При передаче в методы параметров a и b с
 ними нужно производить соответствующие действия и печатать ответ.
"""


class ClassMath:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Деление на ноль")

    def subtraction(self):
        return print(self.a - self.b)


var = ClassMath(6, 3)
var.addition()
var.multiplication()
var.division()
var.subtraction()
