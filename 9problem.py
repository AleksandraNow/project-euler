for a in range(1,1000):
    for b in range(1,1000):
        c=1000-(a+b)
        if a+b >=c and a+c >=b and c+b>= a:
            if a**2 +b **2==c**2:
                print(a,b,c)