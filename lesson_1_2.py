sec = int(input("Введите количество секунд"))
sec_in_min = 60
min_in_hour = 60
minute = sec / sec_in_min
hour = (sec / sec_in_min) / min_in_hour
hour_result = int(hour)
minute_subtotal = sec - (hour_result * sec_in_min * min_in_hour)
minute_result = int(minute_subtotal/sec_in_min)
sec_result = minute_subtotal - (minute_result*sec_in_min)
if len(str(hour_result))==1:
    hour_result ="0"+str(hour_result)
if len(str(minute_result))==1:
    minute_result ="0"+str(minute_result)
print (str(sec) + " секунд в формате 'чч:мм:сс' это: " + str(hour_result) + ':' + str(minute_result) + ':' + str(sec_result))