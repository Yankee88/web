import datetime

MONTHS = ('Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабьр')
FF = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
While True:
    year = input("Год:")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break
While True:
    month = input("месяц: ")
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break
calText = " "
calText += ("" * 34) + MONTHS[month - 1] + " " + str(year)
for i in range(7):
calText += DAYS[i] + " "

print(calText)
weekSeparator = ("+----------" * 7) + "\n"
blankRow = ("          " * 7) + "|\n"