a = input("Введите сумму выручки ")
b = input("Введите сумму издержек")
aa = float(a)
bb = float(b)
if aa > bb:
   profit = float(aa - bb)
   rent = profit/aa*100
   print("Прибыль составляет: " + str(profit))
   d = int(input('Введите количество сотрудников'))
   e = profit/d
   print(f"Прибыль на человека составляет: " + str(e))

else:
   print ("Убыток")
