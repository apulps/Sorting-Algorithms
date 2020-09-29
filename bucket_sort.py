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
    

def bucket_sort(n):
    """
    Bucket sort

    Complexity -> O(n^2)
    """
    slots = 10
    array = [[] for i in range(slots)]
    
    for j in n:
        index = int(slots * j)
        array[index].append(j)

    for i in range(slots):
        array[i] = insertion_sort(array[i])

    k = 0
    for i in range(slots):
        for j in range(len(array[i])):
            n[k] = array[i][j]
            k += 1

    return n
