palindromes = [] 
for x in range(100,1000):
    for i in range(100,1000):
        num = str(i*x).split()[0]
        if len(num) == 6:
            if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
                palindromes.append(i *x)
print(max (palindromes))
