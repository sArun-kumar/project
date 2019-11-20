N = int(input('enter the size of the triangle '))
if N>0:
    for i in range(1, N+1):
        print((10**i//9)**2)
    
else:
    print('enter possitive number ')
