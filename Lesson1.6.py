while True:
    a = float(input('Insert a'))
    b = float(input('Insert b'))
    d = 1
    if a <=0 or b <= 0:
        print('Err')
    else:
        while a <= b:
            a += a * 0.1
            d += 1
    print(f'On the {d}  day')
    break