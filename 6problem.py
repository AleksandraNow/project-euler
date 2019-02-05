EveryNumberExponent=[] 
for numbers in range (101): 
    EveryNumberExponent.append(numbers**2) 
sum1=0
for number in EveryNumberExponent:
    sum1+=number   

sum_of_powered_numbers=[]
for digits in range(101):
    sum_of_powered_numbers.append(digits)
    
sum2=0
for digits in sum_of_powered_numbers:
    sum2+=digits

print(sum2)
x=(sum2**2)
print(x-sum1)