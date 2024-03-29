array = [5, 9, 4, 8, 6]

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

print(insertion_sort(array))

# Time Complexity: Worst case = O(n ** 2) || Best case = O(n)