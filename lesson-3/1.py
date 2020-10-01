def div(*args):

    try:
        arg1 = int(input("Введите первое число "))
        arg2 = int(input("Введите Второе число "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Ошибка! Делить на ноль нельзя"

    return res

print(f'result  {div()}')