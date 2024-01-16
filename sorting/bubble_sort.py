array = [5, 9, 4, 8, 6, 1, 12, 10]

def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    
    for i in range(1, len(arr)):
        for j in range(1, len(arr) - i + 1):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    return arr

print(bubble_sort(array))

# Time Complexity: Worst case = O(n ** 2) || Best case = O(n)