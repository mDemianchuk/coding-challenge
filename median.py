def is_empty(arr):
    return len(arr) == 0


def contains_single_element(arr):
    return len(arr) == 1


def is_even(arr):
    return len(arr) % 2 == 0


def is_odd(arr):
    return not is_even(arr)


def get_average(num1, num2):
    return (num1 + num2) / 2


def get_median_index(arr):
    median_index = int(len(arr) / 2) - 1
    if is_odd(arr):
        median_index = median_index + 1
    return median_index


def get_median(arr):
    median_index = get_median_index(arr)
    if is_even(arr):
        median = get_average(arr[median_index], arr[median_index + 1])
    else:
        median = arr[median_index]
    return median


def find_median(arr1, arr2):
    # when one of the arrays is empty return the median of another
    # assuming they both cannot be empty
    if is_empty(arr1):
        return get_median(arr2)
    elif is_empty(arr2):
        return get_median(arr1)

    # when both contain only one number return the average of these elements
    if contains_single_element(arr1) and contains_single_element(arr2):
        return get_average(arr1[0], arr2[0])

    arr1_left_last_index = get_median_index(arr1)
    arr2_left_last_index = get_median_index(arr2)
    # if both are odd it means that their left halfs would be 1 element bigger than the right
    # so if the first left half is bigger by one element than the right one
    # we want to make sure in the second array it's opposite
    if is_odd(arr1) and is_odd(arr2):
        arr2_left_last_index = arr2_left_last_index - 1

    print(arr1_left_last_index)
    print(arr2_left_last_index)

    while True:
        arr1_right_first_index = arr1_left_last_index + 1
        arr2_right_first_index = arr2_left_last_index + 1

        if arr1[arr1_left_last_index] < arr2[arr2_right_first_index] \
                and arr2[arr2_left_last_index] < arr1[arr1_right_first_index]:
            left_max_number = max(arr1[arr1_left_last_index], arr2[arr2_left_last_index])
            # when the merged array is even return the average of two numbers in the middle
            if (len(arr1) + len(arr2)) % 2 == 0:
                # we need to find a number that is next to the biggest one in the left half
                right_min_number = min(arr1[arr1_right_first_index], arr2[arr2_right_first_index])
                # as we got two middle numbers return their average
                return get_average(left_max_number, right_min_number)
            return left_max_number

        # need to adjust indexes that split the arrays
        elif arr1[arr1_left_last_index] > arr2[arr2_right_first_index]:
            # arr1 split point shifts to the left
            arr1_left_last_index = arr1_left_last_index - 1
            # arr1 split point shifts to the right
            arr2_left_last_index = arr2_left_last_index + 1

        else:
            # arr1 split point shifts to the right
            arr1_left_last_index = arr1_left_last_index + 1
            # arr1 split point shifts to the left
            arr2_left_last_index = arr2_left_last_index - 1


nums1 = [0, 0, 0, 0, 4]
nums2 = [2, 3, 4, 5, 6]

print(find_median(nums1, nums2))
