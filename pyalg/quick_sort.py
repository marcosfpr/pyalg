def quick_sort(arr, start=0, end=None):
    end = end if end is not None else len(arr) - 1

    if start < end:
        partition = hoare_partition(arr, start, end)
        quick_sort(arr, start, partition - 1)
        quick_sort(arr, partition + 1, end)

    return arr


def hoare_partition(arr, start, end):
    pivot = arr[start]

    i = start + 1
    j = end

    while j >= i:
        while i <= j and arr[i] < pivot:
            i += 1

        while j >= i and arr[j] >= pivot:
            j -= 1

        if j >= i:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]

    return j


if __name__ == "__main__":
    import random
    from copy import copy

    arr = [1, 2, 4, 7, 10, 15, 20, 47, 50, 92, 101]

    random_arr = copy(arr)
    random.shuffle(random_arr)

    print(f"Sorting: {random_arr}")

    sorted = quick_sort(random_arr)

    print(f"Sorted {sorted}")

    assert arr == sorted
