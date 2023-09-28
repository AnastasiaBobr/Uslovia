year = int(input('year: '))

if year % 4 == 0:
    if year % 100 != 0:
        print('its leap year')
    else:
        if year % 400 == 0:
            print('its a leap year')
        else:
            print('its not leap year')
else:
   print('its not leap year')
