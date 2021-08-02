a = int(input('Введите целое положительное число'))
m = a%10
a = a // 10
while a > 0:
    if a % 10 > m or a % 10 == m:
         m = a % 10
         a = a // 10
    elif a % 10 < m:
         a = a // 10
print(str(m))



