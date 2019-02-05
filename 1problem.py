x=[]
for y in range(1,1000):
    if y% 3==0 or y % 5==0:
        x.append(y)
        sum_of_number=sum(x)

print(sum_of_number)



