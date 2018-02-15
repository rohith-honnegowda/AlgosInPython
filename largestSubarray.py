'''
Find the sub array which produces the largest sum
'''

def largestSumOfSubArray(arr):
        
    current_max = None
    global_max = None

    if len(arr) > 0:
        current_max = arr[0]
        global_max = arr[0]
        for i in range(1, len(arr)):
            if current_max < 0:
                current_max = arr[i]
            else:
                current_max = current_max + arr[i]
            
            if global_max < current_max:
                global_max = current_max

    return global_max        
    
def main():
    #arr = [-4, 1, 2, 30, -10, 3, 9, 2, -10]
    #arr = [-10, 10]
    arr = []
    maxSum = largestSumOfSubArray(arr)
    print("The largest sum of the subarray in the Array above is: {0}".format(maxSum))
    
if __name__ == "__main__":
    main()