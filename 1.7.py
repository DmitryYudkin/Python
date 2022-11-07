from math import factorial
def factorial_gen(n):
    for i in range(n):
        print(i+1, end='! = ')
        yield factorial(i+1)
print("Факториал заданного числа")
for el in factorial_gen(5):
    print(el)