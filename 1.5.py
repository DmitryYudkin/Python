from functools import reduce
List = [i for i in range(100, 1001, 2)]
print("Список чётных чисел [100..1000]:\n", List)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, List))