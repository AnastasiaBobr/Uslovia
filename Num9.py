shotRange = float(input('range: '))

if shotRange > 28 and shotRange < 30:
    print('Попал!!')
elif shotRange >= 30:
    print('Перелет!!')
elif shotRange > 0 and shotRange <= 28:
    print('Недолет!!')
elif shotRange <=0:
    print('Не бей по своим!!')

