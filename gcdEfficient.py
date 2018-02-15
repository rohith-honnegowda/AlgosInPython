print('Enter two numbers whose GCD needs to be found')
a = int(raw_input())
b = int(raw_input())

if(a <= 0) or (b <= 0):
    print('Please enter two positive non-zero numbers to find the gcd')
    exit()

def gcdiv(a,b):
    if a%b == 0:
        print('The gcd of the numbers {0} and {1} is {2}'.format(a, b, b))       
        return b
    rem = a%b
    a = b
    b = rem
    gcdiv(a,b)
 
print('The gcd of the numbers {0} and {1} is {2}'.format(a, b, gc))        

