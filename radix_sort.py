def counting_sort(array, exp):
    n = len(array)

    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = int((array[i] / exp))
        count[ (index)%10 ] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1

    while i >= 0:
        index = int((array[i] / exp))
        output[count[(index) % 10] - 1] = array[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]


def radix_sort(array):
    """
    Radix sort

    Complexity -> O(nk)
    """
    m = max(array)

    exp = 1

    while m / exp > 0:
        counting_sort(array, exp)
        exp *= 10

    return array
