List = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (List.append(list[i]))
print("Заданный список: ", list)
print("Список, где элементы больше предыдущего: ", List)