# My first Python program

'''
This is a multiline comment 
shif + A + option = comment in Mac
'''


print ('Hello Python.') # Inline comment

#Bad write
primes1 = []
for x in range(1, 10):
    count = 0
    for y in range(1, x+1):
        if x%y == 0:
            count += 1
    if count == 2:
        primes1.append(x)
print("primes1 = ",primes1)

#Good write 
primes2 = list(filter(lambda x:
                    all(x%y != 0 for y in range(2,x)),
                    range(2,10)))
print("primes2 = ",primes2)


Dict = {'x':10, 'y':20}
print(y in Dict) 
