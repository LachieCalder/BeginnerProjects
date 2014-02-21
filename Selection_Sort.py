# selection sort implementation
# Lachie Calder

def selection_sort(array):
    """simple implementation of selection_sort"""
    marker = 0
    while marker < len(array):
        smallest = marker
        for n in range(marker, len(array)):
            if array[n] < array[smallest]:
                smallest = n
        array[smallest], array[marker] = array[marker], array[smallest]
        marker += 1
    return array

print(selection_sort([3, 4, 8, 2, 5, 0]))
print(selection_sort([3, 4, 56, 34, 5, 19, 2, 875]))
