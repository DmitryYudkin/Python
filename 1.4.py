List = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходные элементы списка:\n", List)
List2 = [i for i in List if List.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", List2)