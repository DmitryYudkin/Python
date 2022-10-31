List = [7, 5, 3, 3, 2]
Number = int(input('Введите целое число:'))   # 3
i = 0
for m in List:
    if Number <= m:
        i += 1
List.insert(i, Number)
print (f"Новый рейтинг - {List}")
