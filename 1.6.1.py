from itertools import count
print("Итератор, генерирующий целые числа, начиная с указанного")
n = int(input("Введите целое число:"))
for i in count(n):
    print(i, end=' ')

