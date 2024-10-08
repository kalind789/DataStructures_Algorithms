from SortAlgos.Sorts import bubble_sort

def binary_search(arr: list, target: int):
    """
        Takes a sorted array and searches for a value by removing half the array in each step.
    """
    arr = bubble_sort(arr)          # makes sure an array is sorted using my custom bubble_sort
    i = 0                           # start index
    j = len(arr) - 1                # end index

    while i <= j:
        middle = (i+j)//2               # find the value in the middle                 

        if arr[middle] == target:       # if the value in the middle is target, we have found it, return that index
            return middle
        
        if target < arr[middle]:        # if the targer is LESS than the value at the middle,
                j = middle-1            # then, end_of_array = middle-1, and now our array is just the left half
        
        elif target > arr[middle]:      # if the targer is GREATER than the value at the middle,
                i = middle+1            # then, start_of_array = middle+1, and now our array is just the right half
        
    return -1

if __name__ == "__main__":
    a1 = [2,3,5,6,7,8,4,1,0]
    target = 6
    
    print(binary_search(a1, target))
