print('Enter two numbers whose GCD needs to be found')
a = int(raw_input())
b = int(raw_input())

if(a <= 0) or (b <= 0):
    print('Please enter two positive non-zero numbers to find the gcd')
    exit()

d = None

for i in range(1,a+b):
    if(a%i == 0) and (b%i == 0):
        d = i
        
        
print('The gcd of the numbers {0} and {1} is {2}'.format(a, b, d))       