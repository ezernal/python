goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []

my_analys = {
    "name": [],
    "price": [],
    "qty": [],
    "ed": [],
}

while n <= goods:
    my_dict = dict({
        'name': input("введите название "),
        'price': input("Введите цену "),
        'qty': input('Введите количество '),
        'ed': input("Введите единицу измерения ")
    })
    my_list.append((n, my_dict))
    n += 1
    my_analys["name"].append(my_dict["name"])
    my_analys["price"].append(my_dict["price"])
    my_analys["qty"].append(my_dict["qty"])
    my_analys["ed"].append(my_dict["ed"])

print(my_list)
print(my_analys)


# или вот так, один с счетчиком второй без


goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []

my_analys = {
    "name": [],
    "price": [],
    "qty": [],
    "ed": [],
}

for number in range(goods):
    my_dict = dict({
        'name': input("введите название "),
        'price': input("Введите цену "),
        'qty': input('Введите количество '),
        'ed': input("Введите единицу измерения ")
    })
    my_list.append(my_dict)
    my_analys["name"].append(my_dict["name"])
    my_analys["price"].append(my_dict["price"])
    my_analys["qty"].append(my_dict["qty"])
    my_analys["ed"].append(my_dict["ed"])

print(my_list)
print(my_analys)