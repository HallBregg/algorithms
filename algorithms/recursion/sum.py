def r_sum(input_list):
    if not input_list:  # input_list == []
        return 0
    head = input_list[0]
    tail = input_list[1:]
    return head + r_sum(tail)
