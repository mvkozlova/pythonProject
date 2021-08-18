my_f = open('test5.txt', 'w')
while True:
    text_str = input("Введите текст ")
    my_f.writelines(text_str + '\n')
    if not text_str:
       break
my_f.close()

my_f = open('test5.txt', 'r')
content = my_f.read().splitlines()
print(f" Вот что получилось: {content}" )
my_f.close()
