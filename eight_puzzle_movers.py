from eight_puzzle_helpers import locate_blank


# def can_move_blank(direction, state):
#     blank_row, blank_col = locate_blank(state)
#     if direction == 'U' and blank_row == 0:
#         return False
#     if direction == 'R' and blank_col == 2:
#         return False
#     if direction == 'D' and blank_row == 2:
#         return False
#     if direction == 'L' and blank_col == 0:
#         return False
#     return True
def can_move_blank(direction, nested_list):
    blank_pos = locate_blank(nested_list)
    print(blank_pos)
    if direction == 'UP' and blank_pos in (0,1,2):
         return False
    if direction == 'RIGHT' and blank_pos in (2,5,8):
         return False
    if direction == 'DOWN' and blank_pos in (6,7,8):
         return False
    if direction == 'LEFT' and blank_pos in (0,3,6):
         return False
    else:
     return True


assert can_move_blank('UP', '123405678')
assert can_move_blank('DOWN', '123405678')
assert can_move_blank('LEFT', '123405678')
assert can_move_blank('RIGHT', '123405678')
assert not can_move_blank('UP', '102345678')
assert not can_move_blank('LEFT', '123045678')
assert not can_move_blank('DOWN', '123456708')
assert not can_move_blank('RIGHT', '123450678')


# def new_after_move(direction, state):
#     blank_index = state.index('0')
#     blank_row, blank_col = blank_index // 3, blank_index % 3
#
#     if direction == 'U':
#         if blank_row == 0:
#             raise RuntimeError('Must NOT happen!')
#         else:
#             swap_row, swap_col = blank_row - 1, blank_col
#             swap_index = swap_row * 3 + swap_col
#             swap_char = state[swap_index]
#
#             new_state = state[:swap_index]
#             new_state += '0'
#             new_state += state[swap_index + 1:blank_index]
#             new_state += swap_char
#             new_state += state[blank_index + 1:]
#
#             return new_state
#     elif direction == 'R':
#         if blank_col == 2:
#             raise RuntimeError('Must NOT happen!')
#         else:
#             swap_row, swap_col = blank_row, blank_col + 1
#             swap_index = swap_row * 3 + swap_col
#             swap_char = state[swap_index]
#
#             new_state = state[:blank_index]
#             new_state += swap_char
#             new_state += state[blank_index + 1:swap_index]
#             new_state += '0'
#             new_state += state[swap_index + 1:]
#
#             return new_state
#     elif direction == 'D':
#         if blank_row == 2:
#             raise RuntimeError('Must NOT happen!')
#         else:
#             swap_row, swap_col = blank_row + 1, blank_col
#             swap_index = swap_row * 3 + swap_col
#             swap_char = state[swap_index]
#
#             new_state = state[:blank_index]
#             new_state += swap_char
#             new_state += state[blank_index + 1:swap_index]
#             new_state += '0'
#             new_state += state[swap_index + 1:]
#
#             return new_state
#     elif direction == 'L':
#         if blank_col == 0:
#             raise RuntimeError('Must NOT happen!')
#         else:
#             swap_row, swap_col = blank_row, blank_col - 1
#             swap_index = swap_row * 3 + swap_col
#             swap_char = state[swap_index]
#
#             new_state = state[:swap_index]
#             new_state += '0'
#             new_state += state[swap_index + 1:blank_index]
#             new_state += swap_char
#             new_state += state[blank_index + 1:]
#
#             return new_state
#     else:
#         raise RuntimeError('Must NOT happen!')
def new_after_move(direction, nested_list):
    # I search the index of the 0
    blank_pos = locate_blank(nested_list)

    if direction == 'UP':
        toswapindex=blank_pos - 3     # I define the index where I will put my 0 after
        toswap_value =nested_list[toswapindex]    # I extract the value currently in the destination index
        # new_nested_list = nested_list[toswapindex:]+'0'+nested_list[toswapindex+1:blank_pos]+toswap_value+nested_list[toswap_value+1:] # I rebuild the list
        new_nested_list = (nested_list[:toswapindex] +
                           '0' +
                           nested_list[toswapindex + 1:blank_pos] +
                           toswap_value +
                           nested_list[blank_pos + 1:])
        return new_nested_list
    elif direction == 'RIGHT':
        toswapindex = blank_pos + 1
        toswap_value = nested_list[toswapindex]
        # new_nested_list = nested_list[toswapindex:]+'0'+nested_list[toswapindex+1:blank_pos]+toswap_value+nested_list[toswap_value+1:] # I rebuild the list
        new_nested_list = (nested_list[:blank_pos]
                           + toswap_value
                           + nested_list[blank_pos + 1:toswapindex]
                           + '0'
                           + nested_list[toswapindex + 1:])
        return new_nested_list
    elif direction == 'DOWN':
        toswapindex=blank_pos + 3
        toswap_value =nested_list[toswapindex]
        # new_nested_list = nested_list[toswapindex:]+'0'+nested_list[toswapindex+1:blank_pos]+toswap_value+nested_list[toswap_value+1:] # I rebuild the list
        new_nested_list = (nested_list[:blank_pos]
                           + toswap_value
                           + nested_list[blank_pos + 1:toswapindex]
                           + '0'
                           + nested_list[toswapindex + 1:])
        return new_nested_list
    elif direction == 'LEFT':
        toswapindex = blank_pos - 1
        toswap_value = nested_list[toswapindex]
        # new_nested_list = nested_list[toswapindex:]+'0'+nested_list[toswapindex+1:blank_pos]+toswap_value+nested_list[toswap_value+1:] # I rebuild the list
        new_nested_list = (nested_list[:toswapindex] +
                           '0' +
                           nested_list[toswapindex + 1:blank_pos] +
                           toswap_value +
                           nested_list[blank_pos + 1:])
    return new_nested_list


assert new_after_move('UP', '123405678') == '103425678'
assert new_after_move('LEFT', '123405678') == '123045678'
assert new_after_move('DOWN', '123405678') == '123475608'
assert new_after_move('RIGHT', '123405678') == '123450678'


# def heuristic(state):
#     total = 0
#     for char in state:
#         current_pos = state.index(char)
#         current_coord = (current_pos // 3, current_pos % 3)
#         if char == '0':
#             right_position = (0, 0)
#         elif char == '1':
#             right_position = (0, 1)
#         elif char == '2':
#             right_position = (0, 2)
#         elif char == '3':
#             right_position = (1, 0)
#         elif char == '4':
#             right_position = (1, 1)
#         elif char == '5':
#             right_position = (1, 2)
#         elif char == '6':
#             right_position = (2, 0)
#         elif char == '7':
#             right_position = (2, 1)
#         elif char == '8':
#             right_position = (2, 2)
#         dx = current_coord[0] - right_position[0]
#         dy = current_coord[1] - right_position[1]
#         dx = abs(dx)
#         dy = abs(dy)
#         total = total + dx + dy
#     return total
def heuristic(string):
    total = 0
    for char in string:
        currentPos = string.index(char)
        currentCoord = (currentPos // 3, currentPos % 3)
        if char == '0':
            rightPosition = (0, 0)
        elif char == '1':
            rightPosition = (0, 1)
        elif char == '2':
            rightPosition = (0, 2)
        elif char == '3':
            rightPosition = (1, 0)
        elif char == '4':
            rightPosition = (1, 1)
        elif char == '5':
            rightPosition = (1, 2)
        elif char == '6':
            rightPosition = (2, 0)
        elif char == '7':
            rightPosition = (2, 1)
        elif char == '8':
            rightPosition = (2, 2)
        print (currentPos)
        dx = currentCoord[0] - rightPosition[0]
        dy = currentCoord[1] - rightPosition[1]
        dx = abs(dx)
        dy = abs(dy)
        total = total + dx + dy
    return total


assert heuristic('102345678') == 2
assert heuristic('120345678') == 4


# if __name__ == '__main__':
#     print(can_move_blank('U', '123405678'))
#     print(can_move_blank('L', '123405678'))
#     print(can_move_blank('D', '123405678'))
#     print(can_move_blank('R', '123405678'))
#     print(can_move_blank('U', '102345678'))
#     print(can_move_blank('L', '123045678'))
#     print(can_move_blank('D', '123456708'))
#     print(can_move_blank('R', '123450678'))
#     print('-' * 40)
#     print(new_after_move('U', '123405678'))
#     print(new_after_move('L', '123405678'))
#     print(new_after_move('D', '123405678'))
#     print(new_after_move('R', '123405678'))
