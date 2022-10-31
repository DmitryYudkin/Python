A = int(input('Insert Your number'))
M = A % 10
A = A // 10
while A > 0:
    if A % 10 > M:
        M = A % 10
    A = A // 10
print(M)
