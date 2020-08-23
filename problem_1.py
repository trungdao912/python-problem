number_convert = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

string_convert = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5'
}


def converter_func(str):
    splitted_string = str.split(' ')

    splitted_string[2] = number_convert[splitted_string[2]]
    splitted_string[-2] = string_convert[splitted_string[-2]]

    return ' '.join(splitted_string)
