from itertools import cycle

с = 0
for el in cycle("2787292564346"):
    if с > 10:
        break
    print(el)
    с += 1