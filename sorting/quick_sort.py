array = [5, 9, 4, 8, 6, 1, 12, 10]

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

    return arr

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]

    return j

lo = 0
hi = len(array) - 1
print(quick_sort(array, lo, hi))

# Time Complexity: Worst case = O(n ** 2) || Best case = O(nlogn)