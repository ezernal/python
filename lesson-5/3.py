with open("test_3.txt", "r", encoding="utf-8") as file:
    dohod = []
    malenkayazp = []
    my_list = file.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            malenkayazp.append(i[0])
        dohod.append(i[1])
print(f"Оклад меньше 20000 {malenkayazp}, средний оклад {sum(map(int, dohod)) / len(dohod)}")
