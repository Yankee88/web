# x = 7
# if x <= 7:
#     print('меньше либо равно')
# else:
#     print('больше')
# print(x == 7)
# x = int(input('Введи число: '))
# if x < 0:
#     print('отрицательное')
# elif x > 0:
#         print('положительное')
# else:
#         print('ноль')
# year = int(input('введи год'))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0:
#     print('високосный')
# else:
#     print('не високосненько')
# number_1 = int(input('первое число:'))
# operation = input('введи операцию(+,-,*,/):')
# number_2 = int(input('второе число:'))
#
# lst = ['+', '-'  , '*' ,'/']
# if operation in lst:
#     if operation == '+':
#         print(number_1 + number_2)
#     elif operation == '-':
#         print(number_1 - number_2)
#     elif operation == '/':
#         print(number_1 / number_2)
#     else:
#         print(number_1 * number_2)
# else:
#     print('написал фигню')
# number_1 = int(input('первое число:'))
# number_2 = int(input('второе число:'))
# number_3 = int(input('третье число:'))
# count_pol = 0 #кол во положительных
# count_otr = 0 #кол во отрицательных
#
# if number_1 < 0:
#     count_pol += 1
# elif number_1 < 0:
#     count_otr += 1
# if number_2 < 0:
#     count_pol += 1
# elif number_2 < 0:
#     count_otr += 1
# if number_3 < 0:
#     count_pol += 1
# elif number_3 < 0:
#     count_otr += 1
# print('положительных:', count_pol)
# print('отрицательных:', count_otr)
# number_1 = int(input('первое число:'))
# number_2 = int(input('второе число:'))
# number_3 = int(input('третье число:'))
# lst = [number_1,number_2,number_3]
# maxi = max(lst)
# mini = min(lst)
# print('самое большое:',maxi)
# print('самое маленькое',mini)
# h = int(input('часы:'))
# m = int(input('минуты:'))
# s = int(input('секунды:'))
#
# if (h > 23 or h < 0)or (m > 59 or m < 0) or (s>59 or s < 0):
#  print('формат неверный :(')
# else:
#     print('формат верный :)')
#     print(f'{h}:{m}:{s}')
# ticket = input('введи номер билета(6 цифр)')
# if len(ticket) == 6 and ticket.isdigit():
#   first_half = ticket[:3]
#   last_half = ticket[-3:]
#   first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#   last_sum = int(last_half[0]) + int(last_half[1]) + int(last_half[2])
#   if first_sum == last_sum:
#       print('билет счатсливый')
#   else:
#       print('билет не счастливый')
# else:
#  print('фигню вписал')
# month = input('введи номер месяца')
# if month.isdigit() and 12 >= int(month) >= 1:
#     month = int(month)
# if 3 >= month >= 5:
#         print('весна')
# elif 6 >= month >= 8:
#         print('лето')
# else:
#         print('зима')
# hamsters = int(input('количество хомяков:'))
# if 11<= hamsters <= 19:
#     print(hamsters, 'хомяков')
# elif hamsters % 10 == 1:
#     print(hamsters, 'хомяк')
# elif 2 <= hamsters <= 4:
#     print(hamsters, 'хомяка')
# else:
#     print(hamsters, 'хомяков')


