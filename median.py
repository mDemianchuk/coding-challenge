def is_empty(arr):
    return len(arr) == 0


def contains_single_element(arr):
    return len(arr) == 1


def is_even_length(arr):
    return len(arr) % 2 == 0


def is_odd_length(arr):
    return not is_even_length(arr)


def get_average(num1, num2):
    return (num1 + num2) / 2.0


def get_median_index(arr):
    median_index = int(len(arr) / 2) - 1
    if is_odd_length(arr):
        median_index = median_index + 1
    return median_index


def get_median(arr):
    median_index = get_median_index(arr)
    if is_even_length(arr):
        median = get_average(arr[median_index], arr[median_index + 1])
    else:
        median = arr[median_index]
    return median


def is_shiftable_left(index):
    return index >= 0


def is_shiftable_right(arr, index):
    return index < len(arr)


def get_median_single_element_array(arr, single_element_arr):
    arr_median_index = get_median_index(arr)

    if is_odd_length(arr):
        median = arr[arr_median_index]
        # since the merged array will be even length, we need to find find two middle numbers
        if arr[arr_median_index] < single_element_arr[0]:
            next_to_median = min(arr[arr_median_index + 1], single_element_arr[0])
        else:
            next_to_median = max(arr[arr_median_index - 1], single_element_arr[0])
        return get_average(median, next_to_median)

    else:
        # the number goes to the right of the median
        if arr[arr_median_index] < single_element_arr[0]:
            median = min(arr[arr_median_index + 1], single_element_arr[0])
        # the number goes to the left
        else:
            median = arr[arr_median_index]
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

    if contains_single_element(arr1):
        return get_median_single_element_array(arr2, arr1)

    if contains_single_element(arr2):
        return get_median_single_element_array(arr1, arr2)

    arr1_left_last_index = get_median_index(arr1)
    arr2_left_last_index = get_median_index(arr2)

    # if both are odd length it means that their left halfs would be 1 element bigger than the right
    # so if the first left half is bigger by one element
    # then we want to make sure the second one's right half is one element smaller than the left  half
    if is_odd_length(arr1) and is_odd_length(arr2):
        arr2_left_last_index = arr2_left_last_index - 1

    while True:
        arr1_right_first_index = arr1_left_last_index + 1
        arr2_right_first_index = arr2_left_last_index + 1

        arr1_left_edge = arr1[arr1_left_last_index] if arr1_left_last_index >= 0 else float("-inf")
        arr1_right_edge = arr1[arr1_right_first_index] if arr1_right_first_index < len(arr1) else float("inf")

        arr2_left_edge = arr2[arr2_left_last_index] if arr2_left_last_index >= 0 else float("-inf")
        arr2_right_edge = arr2[arr2_right_first_index] if arr2_right_first_index < len(arr2) else float("inf")

        if arr1_left_edge <= arr2_right_edge and arr2_left_edge <= arr1_right_edge:
            median = max(arr1_left_edge, arr2_left_edge)
            # when the merged array is even length, return the average of two numbers in the middle
            if (len(arr1) + len(arr2)) % 2 == 0:
                # we need to find a number that is next to the biggest one in the left half
                next_to_median = min(arr1_right_edge, arr2_right_edge)
                # as we got two middle numbers return their average
                return get_average(median, next_to_median)
            return median

        # need to adjust indexes that split the arrays
        elif arr1_left_edge > arr2_right_edge:
            if is_shiftable_left(arr1_left_last_index) and is_shiftable_right(arr2, arr2_right_first_index):
                # shift the split point to the left
                arr1_left_last_index = arr1_left_last_index - 1
                # shift the split point to the right
                arr2_left_last_index = arr2_left_last_index + 1

        else:
            if is_shiftable_left(arr2_left_last_index) and is_shiftable_right(arr1, arr1_right_first_index):
                # shift the split point to the left
                arr2_left_last_index = arr2_left_last_index - 1
                # shift the split point to the right
                arr1_left_last_index = arr1_left_last_index + 1


nums1 = [5, 5, 5, 5, 5]
nums2 = [6, 6, 6, 6, 6]

print(find_median(nums1, nums2))
print(find_median(nums2, nums1))
