from eight_puzzle_helpers import to_2d_list
from eight_puzzle_helpers import locate_blank
from eight_puzzle_helpers import copy_nested_list
from eight_puzzle_helpers import print_nested_list


def can_move_blank(direction, nested_list):
    blank_row, blank_col = locate_blank(nested_list)
    if direction == 'UP' and blank_row == 0:
        return False
    if direction == 'RIGHT' and blank_col == 2:
        return False
    if direction == 'DOWN' and blank_row == 2:
        return False
    if direction == 'LEFT' and blank_col == 0:
        return False
    return True


def new_after_move(direction, nested_list):
    new_nested_list = copy_nested_list(nested_list)

    blank_row, blank_col = locate_blank(nested_list)

    if direction == 'UP':
        if blank_row == 0:
            1/0
        else:
            temp = new_nested_list[blank_row - 1][blank_col]
            new_nested_list[blank_row - 1][blank_col] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'RIGHT':
        if blank_col == 2:
            1/0
        else:
            temp = new_nested_list[blank_row][blank_col + 1]
            new_nested_list[blank_row][blank_col + 1] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'DOWN':
        if blank_row == 2:
            1/0
        else:
            temp = new_nested_list[blank_row + 1][blank_col]
            new_nested_list[blank_row + 1][blank_col] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'LEFT':
        if blank_col == 0:
            1/0
        else:
            temp = new_nested_list[blank_row][blank_col - 1]
            new_nested_list[blank_row][blank_col - 1] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    else:
        1/0


if __name__ == '__main__':
    print(can_move_blank('UP', to_2d_list('123405678')))
    print(can_move_blank('LEFT', to_2d_list('123405678')))
    print(can_move_blank('DOWN', to_2d_list('123405678')))
    print(can_move_blank('RIGHT', to_2d_list('123405678')))
    print(can_move_blank('UP', to_2d_list('102345678')))
    print(can_move_blank('LEFT', to_2d_list('123045678')))
    print(can_move_blank('DOWN', to_2d_list('123456708')))
    print(can_move_blank('RIGHT', to_2d_list('123450678')))
    print_nested_list(new_after_move('UP', to_2d_list('123405678')))
    print_nested_list(new_after_move('LEFT', to_2d_list('123405678')))
    print_nested_list(new_after_move('DOWN', to_2d_list('123405678')))
    print_nested_list(new_after_move('RIGHT', to_2d_list('123405678')))
