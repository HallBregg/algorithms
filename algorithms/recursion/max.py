def r_max(input_list):
    if not input_list:
        return
    if len(input_list) == 1:
        return input_list[0]
    nex_max = r_max(input_list[1:])
    return input_list[0] if input_list[0] > nex_max else nex_max


def r_max_no_len(input_list):
    if not input_list:
        return
    try:
        input_list[1]
    except IndexError:
        return input_list[0]
    new_max = r_max_no_len(input_list[1:])
    return input_list[0] if input_list[0] > new_max else new_max
