''' 
Calculate the square root of a number
Algorithm to use is the square root s of a number n is always lesser than
the number n and also sqrt of a number n < 1 is always less that one
1 < s < 1 + n/2
'''

def squareRoot(low, high, n):
    while True:
        mid = (low + high)/2
        square = mid * mid
        if square == n:
            return mid
        elif square <= n:
            low = mid
        elif square > n:
            high = mid
            
def main():
    n = 5
    sq = squareRoot(0, n/2, n)
    print("The square root of {0} = {1}".format(n, sq))
    
if __name__=="__main__":
    main()   