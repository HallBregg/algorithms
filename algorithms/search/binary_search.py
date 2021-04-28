def binary_search(input_list: list, item):
    """
    input_list must be sorted
    O(log n)
    """
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = input_list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            assert guess == item
            print(f'{item} is in input_list with index {mid}')
            return mid
    print(f'{item} is not in input_list')


# def binary_search_recursive(input_list, item):
#     lowest_index = 0
#     highest_index = len(input_list) - 1
#     # Only one item in a list
#     if lowest_index == highest_index and input_list[lowest_index] == item:
#         return lowest_index
#     mid = (lowest_index + highest_index) // 2
#     if item == input_list[mid]:
#         return mid
#     elif item > input_list[mid]:
#         return binary_search_recursive(input_list[mid:], item)
#     else:
#         return binary_search_recursive(input_list[:mid], item)
