def is_solution(state):
    # return state == '012345678'
    if state == '012345678':
        return True
    else:
        return False


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


def locate_blank(state_list):
    for r, inner in enumerate(state_list):
        for c, num_str in enumerate(inner):
            if num_str == '0':
                return r, c
    raise RuntimeError('Must NOT happen!')


assert locate_blank([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]) == (0, 0)
assert locate_blank([['1', '2', '3'], ['4', '0', '5'], ['6', '7', '8']]) == (1, 1)


def copy_nested_list(nested_list):
    outer_copy = []
    for inner in nested_list:
        inner_copy = inner[:]
        outer_copy.append(inner_copy)
    return outer_copy


assert [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']] == copy_nested_list(
    [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']]
)
assert not [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']] is copy_nested_list(
    [['1', '1', '2'], ['3', '0', '5'], ['6', '7', '8']]
)


def print_nested_list(nested_list):
    for inner in nested_list:
        print(' '.join(inner))


def can_move_blank(direction, state):
    blank_row, blank_col = locate_blank(to_2d_list(state))
    if direction == 'U' and blank_row == 0:
        return False
    if direction == 'R' and blank_col == 2:
        return False
    if direction == 'D' and blank_row == 2:
        return False
    if direction == 'L' and blank_col == 0:
        return False
    return True


assert can_move_blank('U', '123405678')
assert can_move_blank('D', '123405678')
assert can_move_blank('L', '123405678')
assert can_move_blank('R', '123405678')
assert not can_move_blank('U', '102345678')
assert not can_move_blank('L', '123045678')
assert not can_move_blank('D', '123456708')
assert not can_move_blank('R', '123450678')


def new_after_move(direction, nested_list):
    if isinstance(nested_list, str):
        nested_list = to_2d_list(nested_list)

    new_nested_list = copy_nested_list(nested_list)

    blank_row, blank_col = locate_blank(nested_list)

    if direction == 'U':
        if blank_row == 0:
            1/0
        else:
            temp = new_nested_list[blank_row - 1][blank_col]
            new_nested_list[blank_row - 1][blank_col] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'R':
        if blank_col == 2:
            1/0
        else:
            temp = new_nested_list[blank_row][blank_col + 1]
            new_nested_list[blank_row][blank_col + 1] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'D':
        if blank_row == 2:
            1/0
        else:
            temp = new_nested_list[blank_row + 1][blank_col]
            new_nested_list[blank_row + 1][blank_col] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    elif direction == 'L':
        if blank_col == 0:
            1/0
        else:
            temp = new_nested_list[blank_row][blank_col - 1]
            new_nested_list[blank_row][blank_col - 1] = '0'
            new_nested_list[blank_row][blank_col] = temp
            return new_nested_list
    else:
        1/0


assert to_str(new_after_move('U', to_2d_list('123405678'))) == '103425678'
assert to_str(new_after_move('L', to_2d_list('123405678'))) == '123045678'
assert to_str(new_after_move('D', to_2d_list('123405678'))) == '123475608'
assert to_str(new_after_move('R', to_2d_list('123405678'))) == '123450678'


def heuristic(state):
    total = 0
    for char in state:
        current_pos = state.index(char)
        current_coord = (current_pos // 3, current_pos % 3)
        if char == '0':
            right_position = (0, 0)
        elif char == '1':
            right_position = (0, 1)
        elif char == '2':
            right_position = (0, 2)
        elif char == '3':
            right_position = (1, 0)
        elif char == '4':
            right_position = (1, 1)
        elif char == '5':
            right_position = (1, 2)
        elif char == '6':
            right_position = (2, 0)
        elif char == '7':
            right_position = (2, 1)
        elif char == '8':
            right_position = (2, 2)
        dx = current_coord[0] - right_position[0]
        dy = current_coord[1] - right_position[1]
        dx = abs(dx)
        dy = abs(dy)
        total = total + dx + dy
    return total


assert heuristic('102345678') == 2
assert heuristic('120345678') == 4


if __name__ == '__main__':
    print(can_move_blank('U', '123405678'))
    print(can_move_blank('L', '123405678'))
    print(can_move_blank('D', '123405678'))
    print(can_move_blank('R', '123405678'))
    print(can_move_blank('U', '102345678'))
    print(can_move_blank('L', '123045678'))
    print(can_move_blank('D', '123456708'))
    print(can_move_blank('R', '123450678'))
    print('-' * 40)
    print(new_after_move('U', '123405678'))
    print(new_after_move('L', '123405678'))
    print(new_after_move('D', '123405678'))
    print(new_after_move('R', '123405678'))


import datetime
import sys
import os
from queue import Queue, LifoQueue, PriorityQueue

import py_mem_prof
# from memory_profiler import profile

from eight_puzzle_helpers import is_solution
from eight_puzzle_movers import can_move_blank, new_after_move, heuristic

if os.name == 'posix':  # Mac and Linux only
    import resource
else:                   # Windows does not support ru_maxrss
    resource = None


def bfs(queue, seen):
    visit_count = 0
    while queue:
        head = queue.get()
        visit_count += 1
        if is_solution(head['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    head['moves'], len(head['moves']), visit_count
                )
            )
            break
        for direction in ('U', 'L', 'D', 'R'):
            moves_so_far = head['moves']
            current_state = head['state']
            if can_move_blank(direction, current_state):
                new_state = new_after_move(direction, current_state)
                if new_state not in seen:
                    seen.add(new_state)
                    new_moves = moves_so_far + direction
                    queue.put({'state': new_state, 'moves': new_moves})


########################################################################################################################


# @profile
def dfs(stack, seen):
    visit_count = 0
    max_depth = -1
    while stack:
        top = stack.get()
        visit_count += 1
        if is_solution(top['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    top['moves'], len(top['moves']), visit_count
                )
            )
            break
        for direction in ('U', 'L', 'D', 'R'):
            moves_so_far = top['moves']
            if len(moves_so_far) > max_depth:
                max_depth = len(moves_so_far)
            current_state = top['state']
            if can_move_blank(direction, current_state):
                new_state = new_after_move(direction, current_state)
                if new_state not in seen:
                    seen.add(new_state)
                    new_moves = moves_so_far + direction
                    stack.put({'state': new_state, 'moves': new_moves})

    stack_size = py_mem_prof.total_size(stack)
    seen_size = py_mem_prof.total_size(seen)

    if resource:
        resource_usage = resource.getrusage(resource.RUSAGE_SELF)
        ru_maxrss = resource_usage.ru_maxrss
    else:
        resource_usage = None
        ru_maxrss = None

    return max_depth, stack_size, seen_size, ru_maxrss


########################################################################################################################

def a_star(priority_queue, seen):
    visit_count = 0
    while priority_queue:
        t = priority_queue.get()
        lowest = {'state': t[1], 'moves': t[2]}
        visit_count += 1
        if is_solution(lowest['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    lowest['moves'], len(lowest['moves']), visit_count
                )
            )
            break
        for direction in ('U', 'L', 'D', 'R'):
            moves_so_far = lowest['moves']
            current_state = lowest['state']
            if can_move_blank(direction, current_state):
                new_state = new_after_move(direction, current_state)
                if new_state not in seen:
                    seen.add(new_state)
                    new_moves = moves_so_far + direction
                    total = heuristic(new_state)
                    priority_queue.put((total, new_state, new_moves))


########################################################################################################################


if len(sys.argv) == 1:
    start_state = {'state': '275318406', 'moves': ''}

    init_queue = Queue()
    init_queue.put(start_state)
    seen_set = {start_state['state']}
    t0 = datetime.datetime.now()
    bfs(init_queue, seen_set)
    t1 = datetime.datetime.now()
    print('BFS in', (t1 - t0).total_seconds(), 'seconds')

    init_stack = LifoQueue()
    init_stack.put(start_state)
    seen_set = {start_state['state']}
    t0 = datetime.datetime.now()
    result = dfs(init_stack, seen_set)
    t1 = datetime.datetime.now()
    print('DFS in', (t1 - t0).total_seconds(), 'seconds')
    print('max_depth:', result[0])
    print('final_stack_size:', result[1])
    print('max_seen_size:', result[2])
    print('resource.ru_maxrss (KB):', result[3])

    init_pq = PriorityQueue()
    score = heuristic(start_state['state'])
    init_pq.put((score, start_state['state'], start_state['moves']))
    seen_set = {start_state['state']}
    t0 = datetime.datetime.now()
    a_star(init_pq, seen_set)
    t1 = datetime.datetime.now()
    print('A-star in', (t1 - t0).total_seconds(), 'seconds')
elif len(sys.argv) == 3:
    state = sys.argv[2]
    state = state.replace(',', '')
    start_state = {'state': state, 'moves': ''}
    if sys.argv[1] == 'bfs':
        init_queue = Queue()
        init_queue.put(start_state)
        seen_set = {start_state['state']}
        t0 = datetime.datetime.now()
        bfs(init_queue, seen_set)
        t1 = datetime.datetime.now()
        print('BFS in', (t1 - t0).total_seconds(), 'seconds')
    elif sys.argv[1] == 'dfs':
        init_stack = LifoQueue()
        init_stack.put(start_state)
        seen_set = {start_state['state']}
        t0 = datetime.datetime.now()
        result = dfs(init_stack, seen_set)
        t1 = datetime.datetime.now()
        print('DFS in', (t1 - t0).total_seconds(), 'seconds')
        print('max_depth:', result[0])
        print('final_stack_size:', result[1])
        print('max_seen_size:', result[2])
        print('resource.ru_maxrss (KB):', result[3])
    elif sys.argv[1] == 'a-star':
        init_pq = PriorityQueue()
        score = heuristic(start_state['state'])
        init_pq.put((score, start_state['state'], start_state['moves']))
        seen_set = {start_state['state']}
        t0 = datetime.datetime.now()
        a_star(init_pq, seen_set)
        t1 = datetime.datetime.now()
        print('A-star in', (t1 - t0).total_seconds(), 'seconds')
else:
    print('Usage: eight_puzzle.py [search method] [initial state]')
