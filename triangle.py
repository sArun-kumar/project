a = int(input('enter the number of natural numbers you want '))
sum1=0
for i in range(1, a+1):
    sum1=sum1+(i*i)

sum2=0
for i in range(1,a+1):
    sum2= sum2+i
    
print((sum2*sum2)-sum1)
    
