pribyl = float(input("Введите прибыль "))
izderzki = float(input("Введите издержки "))
if pribyl > izderzki:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {pribyl / izderzki:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {pribyl / workers:.2f}")
elif pribyl == izderzki:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")