# print("Hello World")
# # print('test')
# print('qqq')

'''
:param
greeting = "Hello World"
print(greeting)
print(greeting.upper())
print(greeting.lower())
'''

# \n перенесення на новий рядок
# print("Hello \n World")
# \t -> 4 Пробіли (Табуляція)
# \ -> Дзеркалення (якщо потрібно службовий символ зробити друкованим)

print("Hello World!", sep ="", end ="-" )
# print('test')
print('qqq', "wfsdkf", "fsdfsdda")

# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип данних : True False
# str -> рядок -> масив (набір) символів

#print('//////////')

#number: int=10
#print(number)
#print(type(number))
#number = 20.5
#print(number)
#print(type(number))
#number = "Vasya"
#print(number)
#print(type(number))
#number = True
#print(number)
#print(type(number))

# Арифметичні операції у пайтом можна додавати будь які числа можна додавати числа типу int+int
#float + float float+int

#i1 = 2
#i2 = 3
#f1 = 2.1
#f2 = 3.1

# Додавання +

#print(i1 + i2)
#print(f1 + f2)
#print(i1 + f2)
#print(type(i1 + f2))

#i1 = 2
#i2 = 3
#f1 = 2.1
#f2 = 3.1

# Віднімання -

#print(i2 - i1)
#print(f2 - f1)
#print(f2 - i1)
#print(type(f2 - i1))

#i1 = 2
#i2 = 2
#f1 = 2.5
#f2 = 2.5

# множення *

# print(i1 * i2)
# print(f1 * f2)
# print(f1 * i1)
# print(type(f1 * i1))

#ділення /

# i1 = 4
# i2 = 2
# f1 = 2.5
# f2 = 1.25

# print(i2 / i1)
# print(f1 / f2)
# print(f1 / i2)
# print(type(f1 / i2))

# Зведення у ступінь **

# print(2 ** 2)
# print(3 ** 2)
# print(2 ** 3)


# Ділення націло

# Ця операці повертае цілу частину від операції ділення округлючи результут до найблищчого найменшого цілого

# print(11 // 2)

# залишок від ділення ця операція ще називается ділення по модулю вона портае залишок від числа післа ділення націло

# задача
# ввести з клавіатури трьох значне число  та вивести сумму цифр цього числа


# number = 768
# n1 = number // 100
# print(n1)
# n3 = number % 10
# print(n3)
# n2 = number % 100 // 10
# print(n2)
# n2 = (number // 10 % 10)

# result = (n1 + n3 + n2)
# print("Result:",result)



# Д/з

# number = 789
# n1 = number // 100
# print(n1)
# temp = number % 100
# n2 = temp // 10
# print(n2)
# n3 = temp % 10
# print(n3)

# result = (n1 + n3 + n2)
# print("Result:",result)



# number = 8753
# thousand = number // 1000
# hundreds = number // 100
# tens = number // 10
# untis = number // 1
#
# result = (thousand + hundreds + tens + untis)
# print("Result:",result)

# должно получится 8 7 5 3 = 23 (В столбик)
# Итог получилось 9723


# Попытка №2

# number = 8753
# thousand = number // 1000
# print(thousand)
# hundreds = number // 100
# print(hundreds)
# tens = number // 10
# print(tens)
# untis = number // 1
# print(untis)

# result = (thousand + hundreds + tens + untis)
# print("Result:",result)

# Попытка №2 не удалась, но приблизила меня к решению


# Попытка №3

number = 8750
thousand = number // 1000 % 100
print(thousand)
hundreds = number // 100 % 10
print(hundreds)
tens = number // 10 % 10
print(tens)
untis = number // 1 % 10
print(untis)

result = (thousand + hundreds + tens + untis)
print("Result:",result)
# Попытка №3 удалась я получил в результате по столбцу 8  7  5  0  Result: 20

#input ("Enter a number: ")
#number = int(input("Enter a number: "))

#n1 = number // 100
#n2 = number // 10 % 10

# n2 = number % 100 // 10
#n3 = number % 10

#print(n1)
#print(n2)
#print(n3)

#result = n1 + n2 + n3
#print("Result:", result)


07.11
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

#print("Hello,", name, "You are", age, "years old!")

#V2
#print("Hello, " + name + " You are " + str(age) + " years old!")
#конкатинація- тільки коли str, а в інших випадках не буде використовуватися.
#конкатинація це складання рядків, рядок + рядок це один великий рядок.

#v3
#print(f"Hello, {name}. You are {age} years old!")
#інтерполяція рядка вбудування змінних у рядок завдяки функції format(f)

#age_after_ten_years = age + 10
#print(age_after_ten_years)

# input ("Enter a number: ")
# number = int(input("Enter a number: "))
#
# n0 = number // 1000
# n1 = number // 100 % 10
# n2 = number // 10 % 10
#
# n2 = number % 100 // 10
# n3 = number % 10
#
# print(n0)
# print(n1)
# print(n2)
# print(n3)
#
# result = n0 + n1 + n2 + n3
# print("Result:", result)

# Д/з

number = int(input('Enter a number: '))  # 54321
#
n1 = number // 10000 % 10
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number // 10 % 10
n5 = number % 10
#
result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)

# n1 = number // 10000 % 1000  # = 54321 // 10000 % 1000 = 5 % 1000 = 5
# n2 = number // 1000 % 100    # = 54321 // 1000 % 100 = 54 % 100 = 54  (должно быть 4)
# n3 = number // 100 % 10      # = 54321 // 100 % 10 = 543 % 10 = 3
# n4 = number // 10 % 10       # = 54321 // 10 % 10 = 5432 % 10 = 2
# n5 = number % 10             # = 54321 % 10 = 1
# объяснение почему не выводило инверсию чисел.

# n1 = 10
# n2 = 20
# n1,n2 = 10,20
#
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 <= n2)
# print(n1 < n2)
# print(n1 == n2)
#
# print(n1 != n2)
#
# print(1 == 1 and 3 == 3)
# print(1 == 1 or 2 == 3)
#
# is_valid = False
# print(is_valid)
# print(not is_valid)
#
# print("hello" in "hello world")

# hours = int(input("Enter hours: "))
# # v1
# if hours >= 12:
#     print("PM")
# else:
#     print("AM")

# hours = int(input("Enter hours: "))
# # v2
# if 12 <= hours <24:
#     print("PM")
# elif 0 <= hours <12:
#     print("AM")
# else:
#     print("Incorrect hours")

# hours >= 12 and hours < 24

# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано

rating = int(input("Введите рейтинг фильма (от 1 до 5): "))

if rating == 5 or rating == 4:
    print("Рейтинг хороший - можно смотреть!")
else:
    print("Плохой рейтинг - не стоит внимания.")

