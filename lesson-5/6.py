with open('test_6.txt', 'r', encoding="utf-8") as init_f:
    total = {}
    for line in init_f:
        (subject, lessons_count) = line.split(':')
        last_num = ''
        result = 0
        for letter in lessons_count:
            if letter.isdigit():
                last_num += letter
            else:
                if last_num:
                    result += int(last_num)
                    last_num = ''
            total[subject] = result
print(f'Общее количество часов по предмету - \n {total}')
