def mergeSort(arr):
    # base case
    if len(arr) == 1:
        return
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]


    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k +=1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1




# Code to print the list 
def printList(arr): 
  # time O(n)
  # space O(1)
  #write your code here
  for i in range(len(arr)):
    print(arr[i], end="\n")

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
