def selection_sort(array):
    n = len(array)
    i = 0

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array
