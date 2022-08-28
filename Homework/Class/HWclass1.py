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
    name = 'Ivan'
    group_number = 18
    age = "10A"
    def get_name(self):
        pass
    def get_age(self):
        pass
    def get_group_nimber(self):
        pass
    def set_name_age(self):
        pass
    def set_group_number(self):
        pass

STATIC_FIELD = 'value_of_statis_field'
def __init__(self, dynamic_field): self.dynamic_field = dynamic_field
class_object = ClassName('value_of_dynamic_field')