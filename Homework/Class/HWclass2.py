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
        return print(self.a - self.b)

    def multiplication(self):
        return print(self.a * self.b)

    def division(self):
        if self.b != 0:
            return print(self.a / self.b)
        else:
            return print("Деление на ноль")

    def subtraction(self):
        return print(self.a - self.b)


var = ClassMath(6, 2)
var.addition()
var.multiplication()
var.division()
var.subtraction()
