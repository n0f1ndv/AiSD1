from algorithms import *

def sort_using_algorithm(data, algorithm):
    sorted_data = sorted(data)

    if algorithm == 1:
        print("Sorting data using insertion sort.")
        sorted_data = insertion_sort(data)
    elif algorithm == 2:
        print("Sorting data using shell sort.")
        sorted_data = shell_sort(data)
    elif algorithm == 3:
        print("Sorting data using selection sort.")
        sorted_data = selection_sort(data)
    elif algorithm == 4:
        print("Sorting data using heap sort.")
        sorted_data = heap_sort(data)
    elif algorithm == 5:
        print("Sorting data using quick sort, left pivot.")
        sorted_data = quick_sort(data, 0)
    elif algorithm == 6:
        print("Sorting data using quick sort, random pivot.")
        sorted_data = quick_sort(data, 1)
    else:
        raise ValueError("Invalid algorithm number")

    return sorted_data