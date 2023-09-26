print('1 - pramougolnik 2 - triangle 3 - circle')
s = int(input('Viberite figuru: '))

if s == 1:
        print("storoni pramougolnika:")
        a = int(input("a = "))
        b = int(input("b = "))
        s = a*b
        print (s)
        
elif s == 2:
        print("visota u osnovanie triangla:")
        h = int(input("h = "))
        b = int(input("b = "))
        s  = (b*h)/2
        print (s)
    
elif s== 3:
        r = int(input("radius = "))
        print((3.14 * r ** 2))
        print (r)
elif s>=4:
        print("error")