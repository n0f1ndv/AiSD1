import sys
from backend import sort_using_algorithm

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>", 
            "1 innertion sort", 
            "2 shell sort", 
            "3 selection sort", 
            "4 heap sort", 
            "5 quick sort left pivot", 
            "6 quick sort random pivot",  sep="\n")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Data:", data[0:10])
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()