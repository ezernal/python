new_keywords = input("введите строку ")
keywords_list = []
num = 1
for el in range(new_keywords.count(" ") + 1):
    keywords_list = new_keywords.split()
    if len(str(new_keywords)) <= 10:
        print(f" {num} {keywords_list [el]}")
        num += 1
    else:
        print(f" {num} {keywords_list [el] [0:10]}")
        num += 1