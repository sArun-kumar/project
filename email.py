   
def email_vefication(a):
    match = re.match('^[_a-z0-9-]+(\.[a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',a)
        
    if match == None :
        return 0
    else:
        print('the correct email is :')
        print(a)

list=[]
b = int(input('enter the number of emails you want to enter'))

for i in range(0, b):
    email = input('enter email')
    list.append(email)

    
for i in list:
    email_vefication(i)
   
