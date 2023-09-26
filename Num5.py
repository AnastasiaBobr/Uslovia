a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a < b+c and b < a+c and c < a+b:
    print('its real triangle')
else:
    print('its not real triangle')
