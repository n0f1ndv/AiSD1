import random

# TODO: change uppercase names into lowercase because they are not consts
def insertion_sort(G, l=1):
    for i in range(1, len(G)):
        h = i
        
        while G[h] < G[h - l] and h - l >= 0:
            G[h], G[h - l] = G[h - l], G[h]
            h -= l
            print("ndasudas")

    return G


def shell_sort(G):
    P = [1]
    k = 0

    while P[-1] < j: # it seems like j is not defined
        P.append(4**(k + 1) + (3*(2**k)) + 1)
        k += 1
    P.pop()

    while j > 1:
        j = P.pop()
        G = insertion_sort(G, j)

    return G


def selection_sort(G):
    for i in range(len(G)):
        m = i
        for j in range(i+1, len(G)):
            if G[j] < G[m]:
                m = j

        G[i], G[m] = G[m], G[i]

    return G


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