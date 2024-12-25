# Проверка истечения срока выполнения задачи.
from datetime import datetime

now = datetime.now()
print('Текущая дата:', now.strftime('%d-%m-%Y'))

def input_date(name):
    while True:
        date = input(f'Введите дату {name} (дд-мм-гггг):')
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
            return date
        except:
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')

issue_date = input_date('дедлайна')
delta = (issue_date - now).days

dn = 'день'
if abs(delta) > 1:
    if abs(delta) < 5:
        dn = 'дня'
    else:
        dn = 'дней'

if delta == 0:
    print('Дедлайн сегодня!')
elif delta > 0 :
    print(f'До дедлайна осталось {delta} {dn}.')
else:
    print(f'Внимание! Дедлайн истёк {-delta} {dn} назад.')