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
untis = number // 1 % 1
print(untis)

result = (thousand + hundreds + tens + untis)
print("Result:",result)
# Попытка №3 удалась я получил в результате по столбцу 8  7  5  0  Result: 20