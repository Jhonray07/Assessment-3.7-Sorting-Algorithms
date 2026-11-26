"""Assessment 3.7: Sorting Algorithms

Takes a full name, builds an array of its letters, and sorts it
using Insertion Sort.

Rules:
  - Two arrays: unsorted and sorted.
  - Duplicate letters are discarded (case-insensitive, first one kept).
  - Symbols (anything that is not a letter) are excluded.
"""


def build_unsorted_array(full_name):
    """Return a list of unique letters in the order they appear.

    Spaces, digits and symbols are excluded. Duplicates are discarded.
    """
    letters = []
    for char in full_name:
        if not char.isalpha():
            continue
        char = char.upper()
        if char not in letters:     
            letters.append(char)
    return letters


def insertion_sort(array):
    """Sort a list in ascending order using Insertion Sort.

    Works on a copy so the original (unsorted) array is preserved.
    """
    result = array[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    full_name = input("Enter your full name: ")

    unsorted_array = build_unsorted_array(full_name)
    sorted_array = insertion_sort(unsorted_array)

    print("Full name :", full_name)
    print("Unsorted  :", unsorted_array)
    print("Sorted    :", sorted_array)


if __name__ == "__main__":
    main()