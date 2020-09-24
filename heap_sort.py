def heapify(array, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and array[i] < array[left]:
        largest = left
    
    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, n, largest)


def heap_sort(array):
    """
    Heap sort

    Complexity -> O(n*log(n))
    """
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array
