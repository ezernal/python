a = abs(int(input("Введите целое положительное число: ")))
max = a % 10
a = a // 10
while a > 0:
    if a % 10 > max:
        max = a % 10
    a = a // 10
print(max)