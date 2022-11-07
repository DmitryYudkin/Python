def Plata():
    x = float(input('Введите выработку в часах: '))
    y = float(input('Введите ставку в час: '))
    c = float(input('Введите размер премии- '))
    pay = (x * y)
    return pay + c
print(f'Заработная плата составила: {Plata() }')
