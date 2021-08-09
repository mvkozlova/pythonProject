def task_2(name, family, birth_year, city, email, phone):
    b = f"Я, {name} {family}, {birth_year} года рождения из города {city} имею почтовый ящик: {email} и номер " \
        f"телефона: {phone} "
    return b


var1, var2, var3, var4, var5, var6 = input("Введите через пробел Имя, Фамилию, год рождения, город проживания,"
                                           " свою электронную почту и номер телефона").split()
rez = task_2(name=var1, family=var2, birth_year=var3, city=var4, email=var5, phone=var6)
print(rez)
