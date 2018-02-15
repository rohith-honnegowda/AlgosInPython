print('Getting the nth Fibonnacci  number, please enter a value for n')
n = int(input())

d = [None] * n
d[0] = 0
d[1] = 1
for i in range(2,n,1):
    d[i]  = d[i - 1] + d[i - 2]
 
print('The {0} th fibonnaci number is {1}'.format(n, d[n - 1]))	