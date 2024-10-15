def binary_search(arr: list, target: int):
    """
        Takes a sorted array and searches for a value by removing half the array in each step.
    """         
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

def linear_search(arr: list, target: int):
    n = len(arr)
    for i in range(n):
          if arr[i] == target:
               return i
    
    return -1

if __name__ == "__main__":
    a1 = [1,2,3,4,5,6,7,8,9,10]
    target = 6
    
    print(linear_search(a1, target))
    print(binary_search(a1, target))