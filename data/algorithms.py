from random import randint

def insertion_sort(lst, l=1):
    for i in range(l, len(lst)):
        j = i
        
        while lst[j] < lst[j-l] and j-l >= 0:
            lst[j], lst[j-l] = lst[j-l], lst[j]
            j -= l
    return lst


def shell_sort(lst): 
    k = 0
    n = len(lst)
    while (4**(k + 1) + (3 * (2**k)) + 1) < n:
        k += 1
    k-=1

    while k>= 0: 
        insertion_sort(lst, (4**(k + 1) + (3 * (2**k)) + 1))
        k-=1
    insertion_sort(lst, 1)
    return lst


def selection_sort(lst):
    for i in range(len(lst)):
        m = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]

    return lst


def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if n > left and lst[left] > lst[i]:
        largest = left

    if n > right and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i] # swap root with largest child

        heapify(lst, n, largest) # restoring heap property


def heap_sort(lst):
    n = len(lst)

    # building max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    #extract elements from heap
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i] # moving root to the end
        heapify(lst, i, 0) # restoring heap property

    return lst


# This quick sort algorithm has two options;
# mode=0 refers to left pivot;
# mode=1 refers to random pivot.
def quick_sort(lst, mode=0):
    def partition(low, high):
        pivot_index = low if mode == 0 else randint(low, high)
        pivot = lst[pivot_index]
        lst[pivot_index], lst[high] = lst[high], lst[pivot_index]
        i = low
        for j in range(low, high):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[high] = lst[high], lst[i]
        return i

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(lst) - 1)
    return lst