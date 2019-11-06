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


def is_shiftable_left(index):
    return index > 0


def is_shiftable_right(arr, index):
    return index < len(arr) - 1


def get_median_single_element_array(arr, single_element_arr):
    arr_median_index = get_median_index(arr)
    single_element_arr_median_index = get_median_index(single_element_arr)

    if is_odd(arr):
        median = arr[arr_median_index]
        # since the merged array will be even, we need to find find two middle numbers
        if arr[arr_median_index] < single_element_arr[single_element_arr_median_index]:
            next_to_median = min(arr[arr_median_index + 1], single_element_arr[single_element_arr_median_index])
        else:
            next_to_median = max(arr[arr_median_index - 1], single_element_arr[single_element_arr_median_index])
        return get_average(median, next_to_median)

    else:
        # the number goes to the right of the median
        if arr[arr_median_index] < single_element_arr[single_element_arr_median_index]:
            median = min(arr[arr_median_index + 1], single_element_arr[single_element_arr_median_index])
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

    # if both are odd it means that their left halfs would be 1 element bigger than the right
    # so if the first left half is bigger by one element
    # then we want to make sure the second one's right half is one element smaller than the left  half
    if is_odd(arr1) and is_odd(arr2):
        arr2_left_last_index = arr2_left_last_index - 1

    while True:
        arr1_right_first_index = arr1_left_last_index + 1
        arr2_right_first_index = arr2_left_last_index + 1

        if arr1[arr1_left_last_index] <= arr2[arr2_right_first_index] \
                and arr2[arr2_left_last_index] <= arr1[arr1_right_first_index]:
            median = max(arr1[arr1_left_last_index], arr2[arr2_left_last_index])
            # when the merged array is even return the average of two numbers in the middle
            if (len(arr1) + len(arr2)) % 2 == 0:
                # we need to find a number that is next to the biggest one in the left half
                next_to_median = min(arr1[arr1_right_first_index], arr2[arr2_right_first_index])
                # as we got two middle numbers return their average
                return get_average(median, next_to_median)
            return median

        # need to adjust indexes that split the arrays
        elif arr1[arr1_left_last_index] <= arr2[arr2_right_first_index]:
            shiftable_right = is_shiftable_right(arr1, arr1_right_first_index)
            shiftable_left = is_shiftable_left(arr2_left_last_index)

            if shiftable_right and shiftable_left:
                # shift the split point to the right
                arr1_left_last_index = arr1_left_last_index + 1
                # shift the split point to the left
                arr2_left_last_index = arr2_left_last_index - 1
            elif not shiftable_left and not shiftable_right:
                if (len(arr1) + len(arr2)) % 2 == 0:
                    return get_average(arr1[arr1_right_first_index], arr2[arr2_left_last_index])
                return min(arr1[arr1_right_first_index], arr2[arr2_left_last_index])
            else:
                number_of_elements_left = arr1_left_last_index + arr2_left_last_index + 2
                number_of_elements_right = len(arr1) + len(arr2) - number_of_elements_left

                if shiftable_right and number_of_elements_left - 1 == number_of_elements_right:
                    # shift the split point to the right
                    arr2_left_last_index = arr2_left_last_index + 1
                if shiftable_left and number_of_elements_right - 1 == number_of_elements_left:
                    # shift the split point to the left
                    arr2_left_last_index = arr2_left_last_index - 1
                else:
                    # if we can't shift anymore
                    if (len(arr1) + len(arr2)) % 2 == 0:
                        return get_average(arr1[arr1_right_first_index], arr2[arr2_left_last_index])
                    return min(arr1[arr1_right_first_index], arr2[arr2_left_last_index])

        else:
            shiftable_right = is_shiftable_right(arr2, arr2_right_first_index)
            shiftable_left = is_shiftable_left(arr1_left_last_index)

            if shiftable_right and shiftable_left:
                # shift the split point to the right
                arr2_left_last_index = arr2_left_last_index + 1
                # shift the split point to the left
                arr1_left_last_index = arr1_left_last_index - 1
            elif not shiftable_left and not shiftable_right:
                if (len(arr1) + len(arr2)) % 2 == 0:
                    return get_average(arr2[arr2_right_first_index], arr1[arr1_left_last_index])
                return min(arr2[arr2_right_first_index], arr1[arr1_left_last_index])
            else:
                number_of_elements_left = arr2_left_last_index + arr1_left_last_index + 2
                number_of_elements_right = len(arr1) + len(arr2) - number_of_elements_left

                if shiftable_right and number_of_elements_left - 1 == number_of_elements_right:
                    # shift the split point to the right
                    arr2_left_last_index = arr2_left_last_index + 1
                if shiftable_left and number_of_elements_right - 1 == number_of_elements_left:
                    # shift the split point to the left
                    arr1_left_last_index = arr1_left_last_index - 1
                else:
                    # if we can't shift anymore
                    if (len(arr1) + len(arr2)) % 2 == 0:
                        return get_average(arr2[arr2_right_first_index], arr1[arr1_left_last_index])
                    return min(arr2[arr2_right_first_index], arr1[arr1_left_last_index])


nums1 = [1, 2]
nums2 = [3, 4]

print(find_median(nums1, nums2))
print(find_median(nums2, nums1))
