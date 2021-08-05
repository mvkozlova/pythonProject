a = input("Введите строку из нескольких слов")
a = a.split()
i = 1
b = list(a)
line_length = len(b)

while line_length > 0:
    c = b.pop(0)
    print(str(i) + ")  " + c[0:10])
    b = list(filter(c.__ne__, b))
    line_length = len(b)
    i += 1
