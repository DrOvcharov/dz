#1
a = input("Введите свое имя: ")
b = int(input("Введите свой возраст: "))
c = float(input("Введите свой номер: "))

print(a, b, c)


#2
time_in_sec = int(input("Введите время в секундах которое хотите перевести в формат чч:мм:cc: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Время {hours}:{minutes}:{sec} ")

#3

n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)

#4
z = abs(int(input("Введите целое положительное число ")))
max = z % 10
while z >= 1:
    z = z // 10
    if z % 10 > max:
        max = z % 10
    if z > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break


#5
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

#6
a = float(input("Введите результаты пробежки первого дня в км "))
b = float(input("Введите общий желаемый результат в км "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print("Результат достигните через: ")
print(day)


