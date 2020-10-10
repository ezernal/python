def summary():
    try:
        with open("test_5.txt", "w+", encoding="utf-8") as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Неправильно набран номер. Ошибка ввода-вывода")
summary()