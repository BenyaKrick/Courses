"""
[2] Напишите функцию inspect_function(), которая в качестве аргумента принимает другую функцию (главное,
не встроенную, built-in). В результате работы она выводит следующие данные: название анализируемой функции,
наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
"""
import inspect


def inspect_function(func):
    print('Name of function:', func.__qualname__)
    args = str(inspect.signature(foo))
    n = len(args)
    args = (args[1:n]).split(',')
    for arg in args:
        arg = arg.strip()
        posit = arg.find('=')
        if posit == -1:
            print("Positional ", arg)
        else:
            print("Keys   ", arg[0:posit], "Defult  =", arg[posit + 1:])


def foo(a, b, k=8):
    pass
