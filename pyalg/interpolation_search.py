def interpolation_search(arr, key):
    return _interpolation_search(arr, key, 0, len(arr) - 1)


def _interpolation_search(arr, key, left, right):
    if left <= right and arr[left] <= key <= arr[right]:
        pos = left + ((key - arr[left]) * (right - left)) // (arr[right] - arr[left])

        if arr[pos] == key:
            return pos

        elif arr[pos] < key:
            return _interpolation_search(arr, key, pos + 1, right)
        else:
            return _interpolation_search(arr, key, left, pos - 1)

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13

    print(
        "element {} position in array {} = {}".format(
            target, arr, interpolation_search(arr, target)
        )
    )
