array = [5, 9, 4, 8, 6, 1, 12, 10]

def selection_sort(arr):
    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    return arr

print(selection_sort(array))