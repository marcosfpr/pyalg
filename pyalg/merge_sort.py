def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return aggregate(left_sorted, right_sorted)


def aggregate(left, right):
    i = j = 0

    aggregated = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            aggregated.append(left[i])
            i += 1
        else:
            aggregated.append(right[j])
            j += 1

    while i < len(left):
        aggregated.append(left[i])
        i += 1

    while j < len(right):
        aggregated.append(right[j])
        j += 1

    return aggregated


if __name__ == "__main__":
    import random
    from copy import copy

    arr = [1, 2, 4, 7, 10, 15, 20, 47, 50, 92, 101]

    random_arr = copy(arr)
    random.shuffle(random_arr)

    print(f"Sorting: {random_arr}")

    sorted = merge_sort(random_arr)

    print(f"Sorted {sorted}")

    assert arr == sorted
