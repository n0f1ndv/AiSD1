import random

# TODO: change uppercase names into lowercase because they are not consts
def insertion_sort(lst, l=1):
    for i in range(1, len(lst)):
        h = i
        
        while lst[h] < lst[h - l] and h - l >= 0:
            lst[h], lst[h - l] = lst[h - l], lst[h]
            h -= l

    return lst


def shell_sort(lst):
    gaps = [1]
    k = 0
    j=len(lst)
    while P[-1] < j:
        gaps.append(4**(k + 1) + (3*(2**k)) + 1)
        k += 1
    gaps.pop()

    while j > 1:
        j = gaps.pop()
        lst = insertion_sort(lst, j)

    return lst


def selection_sort(lst):
    for i in range(len(lst)):
        m = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[m]:
                m = j

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
        lst[i], lst[largest] = lst[largest], lst[i]

        heapify(lst, n, largest)


def heap_sort(lst):
    n = len(lst)

    for i in range(n // 2 -1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst


# This quick sort algorithm has two options;
# mode=0 refers to left pivot;
# mode=1 refers to random pivot.
def quick_sort(lst, mode=0):
    if len(lst) <= 1:
        return lst
    
    pivot_index = 0 if mode == 0 else random.randint(0, len(lst) - 1)
    pivot = lst[pivot_index]

    left = [x for x in lst[0:pivot_index] + lst[pivot_index+1:] if x < pivot]
    right = [x for x in lst[0:pivot_index] + lst[pivot_index+1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)