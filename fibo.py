print('Getting the nth Fibonnacci  number, please enter a value for n')
n = int(input())



def fibRecur(n):
	if n <= 1:
		return n
	else :
		return fibRecur(n-1) + fibRecur(n-2)
	


fib = fibRecur(n)
print('The {0} th fibonnaci number is {1}'.format(n, fib))	