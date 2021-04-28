def smallest(input_list: list):
    smallest_index: int = 0
    smallest_value = input_list[smallest_index]
    for i in range(1, len(input_list)):
        input_list_value = input_list[i]
        if input_list_value < smallest_value:
            smallest_index = i
            smallest_value = input_list_value
    return smallest_index, smallest_value


def selection_sort(input_list):
    sorted_list = []
    for element in range(len(input_list)):
        index, value = smallest(input_list)
        sorted_list.append(value)
        input_list.pop(index)
    return sorted_list


def selection_sort_v2(input_list):
    pass
