List = list(input('Введите значения: ').split())
for i in range(1, len(List), 2):
    List[i-1], List[i] = List[i], List[i-1]
print(List)