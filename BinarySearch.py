'''
  Binary Search
'''

class Binary_Search():
    def __init__(self):
        self.data = None

def partition(arr, low, high):
    pivot_value = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high and arr[i] <= pivot_value:
            i = i + 1
        while arr[j] > pivot_value:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low] = arr[j]
    arr[j] = pivot_value
    return j

def quickSort_recuursiveCall(arr, l, h):
    if h > l:
        pivot_index = partition(arr,l,h)
        quickSort_recuursiveCall(arr,l, pivot_index - 1)
        quickSort_recuursiveCall(arr, pivot_index + 1, h)

def quickSort(arr):
    quickSort_recuursiveCall(arr, 0, len(arr) - 1)





def main():
    arr = [12,34,2,454,23,656,2,56,11,6632,3,-33,345,980,873,939]
    #obj = Binary_Search()

    quickSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
