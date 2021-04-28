def r_count(input_list):
    if not input_list:
        return 0
    return r_count(input_list[1:]) + 1
