Str = input('Введите несколько слов через пробел: ').split()
for i, word in enumerate(Str, 1):
    print(i, word[:10])