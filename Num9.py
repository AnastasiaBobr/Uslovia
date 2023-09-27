x = float(input('Дальность выстрела: '))

if x > 28 and x < 30:
    print('Попал!!')
elif x >= 30:
    print('Перелет!!')
elif x > 0 and x <= 28:
    print('Недолет!!')
elif x <=0:
    print('Не бей по своим!!')

