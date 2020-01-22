# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)): #indexing the array by its length
            if arr[smallest_index] > arr[x]: #checking smallest index is greater than arr[x]
                smallest_index = x #assinging smallest index to x if check above 
        # TO-DO: swap
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 
    return arr

print("selection sort", selection_sort([1,3,14,5,31,6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
   
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("bubble sort", bubble_sort([1,3,14,5,31,6]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr