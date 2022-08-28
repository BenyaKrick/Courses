""""
Напишите программу с классом Student, в котором есть три атрибута: name, group_number и age.
По умолчанию name = Ivan, age = 18, group_number = 10A. Необходимо создать пять методов: get_name, get_age,
get_group_number, set_name_age, set_group_number. Метод get_name нужен для получения данных об имени конкретного
студента, метод get_age нужен для получения данных о возрасте
конкретного студента, метод get_group_number нужен для получения данных о номере группы конкретного студента.
Метод set_name_age позволяет изменить данные атрибутов установленных по умолчанию, метод get_group_number позволяет
изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы.
"""


class ClassStudent:
    # name = 'Ivan'
    # age = 18
    # group_number = '10A'
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.groupNumber

    def set_group_number(self, group_number):
        self.groupNumber = group_number
        return self.groupNumber

    def set_name_age(self, name, age):
        self.age = name
        self.name = age
        return name, age


Ivan = ClassStudent()
Sergei = ClassStudent("Сергей", 40, "v90")
Julia = ClassStudent("Юля", 24, "3k")

print(Ivan.__dict__)
print(Sergei.__dict__)
print(Julia.__dict__)
