my_f = open('test.txt', 'r', encoding="utf-8")
line = my_f.read().splitlines()
sal = []
empl = []
for i in line:
        i = i.split()
        print(f"i = {i}")

        if int(i[1]) < 20000:
           empl.append(i[0])
        sal.append(i[1])
        empli = str(empl).strip('[]')
print(f'Оклад меньше 20.000 у {empli}. Средний оклад {sum(map(int, sal)) / len(sal)}')
