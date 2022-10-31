month = int(input('Введите месяц по счету (от 1 до 12): '))
Dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
List = ['Зима', 'Весна', 'Лето', 'Осень']

for i in Dict:
    if month in Dict[i] and 0 < month < 13:
        print(f'{month}-й месяц - это {i}')
if month in [12, 1, 2]:
     print(f'{month}-й месяц - это {List[0]}')
elif month in [3, 4, 5]:
     print(f'{month}-й месяц - это {List[1]}')
elif month in [6, 7, 8]:
     print(f'{month}-й месяц - это {List[2]}')
elif month in [9, 10, 11]:
     print(f'{month}-й месяц - это {List[3]}')
else:
    month <= 0 or month >=13
    print("Ошибка")

