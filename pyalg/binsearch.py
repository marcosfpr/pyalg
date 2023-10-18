import math


def binsearch(array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = math.ceil((left + right) / 2)
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    arr = [1, 2, 4, 7, 10, 15, 20, 47, 50, 92, 101]

    key = 20

    print("{} and {} => {}".format(arr, key, binsearch(arr, key)))
