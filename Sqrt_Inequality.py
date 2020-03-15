a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

if c-a-b > 0 and 4*a*b < (c-a-b)**2:
    print('Yes')
else:
    print('No')

#print(float(int(a)**(1/2)))
#print(float(int(b)**(1/2)))
#print(float(int(c)**(1/2)))