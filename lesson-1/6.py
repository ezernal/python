a = int(input("Введите длину в км за один день: "))
b = int(input("Введите общий результат в км: "))
rez_day = 1
rez_km = a

while rez_km < b:
    a = a + 0.1 * a
    rez_day += 1
    rez_km = rez_km + a
print(f"Желаемый результат будет достигнут на день %.d" % rez_day)