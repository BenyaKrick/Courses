"""
[1] Напишите набор из шести операторов class для моделирования такой иерархической классификации с помощью наследования
Python. Затем добавьте в каждый класс метод speak, выводящий уникальное сообщение, а в суперкласс верхнего уровня
Animal — метод reply, который просто вызывает self. speak, чтобы запустить инструмент вывода, специфичный для
категории, из подкласса ниже в дереве (это инициирует независимый поиск при наследовании из self). Наконец,
удалите метод speak из класса Hacker, чтобы он выбирал стандартный метод, находящийся выше. Когда вы завершите,
ваши классы должны работать следующим образом:
См. картинку ниже
spot = Cat()
spot.reply () # Animal. reply: вызывает Cat.speak
meow
data = Hacker () # Animal. reply: вызывает Primate.speak
data.reply()
Hello world!
"""


class Animal:

    def __init__(self, reply):
        self.reply = reply
        return reply


class Mammal(Animal):

    def Speak_mam(self, phrase):
        self.phrase = phrase
        return phrase


class Cat(Mammal):

    def speak_cat(self, phrase):
        self.phrase = "miay"
        return phrase


class Dog(Mammal):
    def speak_dog(self, phrase):
        self.phrase = "Gav"
        return phrase


class Primat(Mammal):
    def speak_primat(self, phrase):
        self.phrase = "Y-Y-Y"
        return phrase


class Hacker(Primat):
    def speak_Hacker(self, phrase):
        self.phrase = "speak"
        return phrase
