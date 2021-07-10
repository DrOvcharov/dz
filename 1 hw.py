#1
my_list = [12, None, -77, 'True', True, 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
    my_type(my_list)

#2
el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
    el += 2
print(my_list)

#3
d = {"январь":1, 'февраль':2, "март":3, 'апрель':4, 'май':5, 'июнь':6, 'июль':7, 'август':8, 'сентябрь':9, 'октябрь':10, 'ноябряь':11, 'декабрь':12}
num = int(input("введите номер месяца: "))
for key in d:
    if num == 1 or num == 2 or num == 12:
        print("зима")
        break
    elif num == 4 or num == 5 or num == 3:
        print('весна')
        break
    elif num == 6 or num == 7 or num == 8:
        print('лето')
        break
else:
    print('осень')

#4
my_str = input("введите строку ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

#5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))



