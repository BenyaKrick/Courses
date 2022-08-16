def decorating_func(func):
    def wrapper(*args, **kwargs):
        # operations before run
        result = func(*args, **kwargs)
        # operations_after_run
        return result

    return wrapper


@decorating_func
def sum_func(a, b):
    pass


print(sum_func(0, 1))
