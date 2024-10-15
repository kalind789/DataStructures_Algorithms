def bubble_sort(arr: list) -> list:
     """
        Given an array, bubble sort compares each value to the next and swaps if the left value is > right value.
        In each iteration, the last value should be the greatest, so the next time we can just go through n-1 interations.
     """
     n = len(arr)
     for i in range(n-1):                   # outer loop to control if the last element is accessed. (n-1) to bypass end of array error. 
          for j in range(n-i-1):            # inner loop used to compare two array values
               if arr[j] > arr[j+1]:        # if the value is > next value
                    temp = arr[j]           # swap the value with the next, i chose to use temp for comfort
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    # arr[j], arr[j+1] = arr[j+1], arr[j] could also be used in this

     return arr

def selection_sort(arr: list) -> list: 
     n = len(list)
     for i in range(n-1):
          for j in range(i, n):
               
               

if __name__ == "__main__":
    a1 = [2,3,5,6,7,8,4,1,0]
    target = 6
    
    print(bubble_sort(arr=a1))