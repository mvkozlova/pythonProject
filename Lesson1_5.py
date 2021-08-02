a = int(input("Введите сумму выручки"))
b = int(input("Введите сумму издержек"))

if a > b:
   profit = int(a - b)
   rent = profit/a*100
   print("Прибыль составляет: " + str(profit))
   d = int(input('Введите количество сотрудников'))
   e = profit/d
   print(f"Прибыль на человека составляет: " + str(e))

else:
   print ("Убыток")
