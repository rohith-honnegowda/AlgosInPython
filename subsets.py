'''
Get all the subsets of the array
'''

def getBit(countOfSet, num):
    temp = (1<<num)
    temp = temp & countOfSet
    if temp == 0:
        return 0
    return 1


def get_all_subsetsPossible(arr):
    numOfSubsets = 2 ** len(arr)
    lists = []
    for i in range(0, numOfSubsets):
        st = set([])
        for j in range(0, len(arr)):
            if getBit(i, j) == 1:
                st.add(arr[j])
        lists.append(st)
    return lists

def main():
    arr = [2,34,5]
    sets = get_all_subsetsPossible(arr)
    for i in range(0, len(sets)):
        print(sets[i])
        print("\n")

if __name__ == "__main__":
    main()
