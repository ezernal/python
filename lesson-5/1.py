lines = [input("Введите сюда числа ")]
with open("dz.txt", "a+") as file:
    for  line in lines:
        file.write(line + '\n')