def is_solution(state):
    return state == '012345678'

assert is_solution('012345678')
assert not is_solution('082345671')

def to_2d_list(string):
    outer = []
    for i in range(9):
        if i % 3 == 0:
            inner = [string[i]]
            outer.append(inner)
        else:
            inner = outer[i // 3]
            inner.append(string[i])
    return outer

assert to_2d_list('012345678') == [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

def to_str(nested_list):
    string = ''
    for inner in nested_list:
        string += ''.join(inner)
    return string

assert to_str([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]) == '012345678'
assert to_str(to_2d_list('012345678')) == '012345678'

def locate_blank(nested_list):
    for r, inner in enumerate(nested_list):
        for c, num_str in enumerate(inner):
            if num_str == '0':
                return (r, c)
    1 / 0

assert locate_blank([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]) == (0, 0)
assert locate_blank([['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']]) == (1, 1)

def copy_nested_list(nested_list):
    outer_copy = []
    for inner in nested_list:
        inner_copy = inner[:]
        outer_copy.append(inner_copy)
    return outer_copy

assert [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']] == copy_nested_list([['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']])
assert not [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']] is copy_nested_list([['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']])

def print_nested_list(nested_list):
    for inner in nested_list:
        print(' '.join(inner))
