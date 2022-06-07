


def partition(arr, low, high, pivot):

    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    return low


def quickSort(arr, low, high):
    if low >= high:
        return
    
    pivot = arr[(low+high) // 2]
    idx = partition(arr, low, high, pivot)
    quickSort(arr, low, idx-1)
    quickSort(arr, idx, high)


def quickSortIterative(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        pivot = arr[(low+high) // 2]
        idx = partition(arr, low, high, pivot)
        if idx - 1 > low:
            stack.append((low, idx-1))
        if idx < high:
            stack.append((idx, high))
        


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5 ,1, 5, 77, 33, 11, 878, 123 ] 
n = len(arr) 
# quickSort(arr,0,n-1) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
