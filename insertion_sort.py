def insertion_sort(array):
    """
    Insertion sort

    Complexity -> O(n^2)
    """
    n = len(array)

    for i in range(1, n):
        value = array[i]
        j = i - 1

        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = value 
    
    return array
