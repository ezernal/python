with open("test_2.txt", "r", encoding="utf-8") as file:
    print(f"Количество строк в файле - {len(file.readlines())}")

with open("test_2.txt", "r", encoding="utf-8") as file:
    ders = file.readlines()
    for i in range(len(ders)):
        print(f"Количество символов {i + 1} - {len(ders[i])}")

with open("test_2.txt", "r", encoding="utf-8") as file:
    content = file.read()
    content = content.split()
    print(f"Общее количество слов - {len(content)}")