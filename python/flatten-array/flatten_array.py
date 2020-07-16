def flatten(iterable):
    flat_arr = []
    flatten_array(iterable, flat_arr)
    return flat_arr

def flatten_array(input, flat_arr):
    for e in input:
        if isinstance(e, list):
            flatten_array(e, flat_arr)
        elif e is not None:
            flat_arr.append(e)
