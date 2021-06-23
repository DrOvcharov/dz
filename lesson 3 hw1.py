def div(*args):
    try:
        arg1 = int(input("Введите первое число: "))
        arg2 = int(input("Введите второе число: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "ААААА на ноль делить нельзя! давай еще раз"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("ААААА на ноль делить нельзя! давай еще раз")
    '''


print(f'результат {div()}')
