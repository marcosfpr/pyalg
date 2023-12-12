def find_largest(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2

    left_max = find_largest(arr[:mid])
    right_max = find_largest(arr[mid:])

    return max(left_max, right_max)


if __name__ == "__main__":
    import random
    from copy import copy

    arr = [1, 2, 4, 7, 10, 15, 20, 47, 50, 92, 101]

    random_arr = copy(arr)
    random.shuffle(random_arr)

    print(f"Array: {random_arr}")

    largest = find_largest(random_arr)

    print(f"Largest element {largest}")
