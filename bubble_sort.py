def bubble_sort(array):
    """
    Bubble sort

    Complexity -> O(n*n)
    """
    n = len(array)

    for i in range(n):
        flag = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        
        if flag == False:
            break

    return array
