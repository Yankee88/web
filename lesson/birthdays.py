import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерируем(до 70)?")
    if not  number.isdigit() or int(number) > 70 or int(number) < 2:
        print("По твоему это смешно?Число от 2 до 70,пж")
        print("-" * 8)
    else: #еслии все ок
        number = int(number) #строчка число
        break #выход из True
birthdays = []
startOFYear = datetime.date(2022,1,1)
for _ in range(number):
    shift = random.randint(0,364)
    shiftOfdays = datetime.timedelta(shift)
    birthday =  startOFYear + shiftOfdays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays): #множество,повторения исключены
    if birthdays.count(i) > 1: #два+ вхождения
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)}раза")
