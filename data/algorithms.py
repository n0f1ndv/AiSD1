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
def quick_sort(lst, piv=None):
    def set_pivot():
        if piv is not None and piv >= len(lst):
            return len(lst) - 1

        return randint(0, len(lst) - 1) if piv is None else piv

    if len(lst) <= 1:
        return lst
    
    pivot_index = set_pivot()
    pivot = lst[pivot_index]

    left = [x for x in lst[0:pivot_index] + lst[pivot_index+1:] if x < pivot]
    right = [x for x in lst[0:pivot_index] + lst[pivot_index+1:] if x >= pivot]

    return quick_sort(left, piv) + [pivot] + quick_sort(right, piv)