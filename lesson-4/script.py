from sys import argv
param = argv[1:]
time, salary, bonus = param
res = int(time) * int(salary) + int(bonus)
print(f'заработная плата сотрудника {res}')