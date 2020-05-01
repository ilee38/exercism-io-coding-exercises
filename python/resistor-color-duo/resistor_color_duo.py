def value(colors):
    if len(colors) < 2:
        raise ValueError('Missing color(s)')
    color_values = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    res_value = str(color_values.index(colors[0])) + str(color_values.index(colors[1]))
    return int(res_value)
