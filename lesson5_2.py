my_f = open('test.txt', 'r', encoding="utf-8")
lline = my_f.readlines()
for i in range(len(lline)):
    word_cnt = lline[i].count(' ') + 1
    print(f"{i + 1} строка содержит {len(lline[i])} символов и {word_cnt} слов(а)")
print(f"Всего количество строк: {len(lline)} ")
my_f.close()
