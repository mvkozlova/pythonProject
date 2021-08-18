def summary():
    try:
        with open('test6.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()