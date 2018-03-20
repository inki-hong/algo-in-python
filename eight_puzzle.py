import datetime
import sys

from eight_puzzle_helpers import *
from eight_puzzle_movers import *

st_state = {'state': '275318406', 'moves': []}
qu = [st_state]
saw = {st_state['state']}


def bfs(start_state, queue, seen):
    visit_count = 0
    while queue:
        head, queue = queue[0], queue[1:]
        visit_count += 1
        if is_solution(head['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    head['moves'], len(head['moves']), visit_count
                )
            )
            break
        for direction in ('UP', 'LEFT', 'DOWN', 'RIGHT'):
            moves_so_far = head['moves']
            nested_list = to_2d_list(head['state'])
            if can_move_blank(direction, nested_list):
                new_state = to_str(new_after_move(direction, nested_list))
                if new_state not in seen:
                    seen.add(new_state)
                    new_moves = moves_so_far[:]
                    new_moves.append(direction)
                    queue.append({'state': new_state, 'moves': new_moves})


# t0 = datetime.datetime.now()
#
# bfs(st_state, qu, saw)
#
# t1 = datetime.datetime.now()
#
# print((t1 - t0).total_seconds())

########################################################################################################################

st_state = {'state': '275318406', 'moves': []}
qu = [st_state]
saw = {st_state['state']}

max_depth = -1


def dfs(start_state, stack, seen):
    global max_depth
    visit_count = 0
    while stack:
        top = stack.pop()
        visit_count += 1
        if is_solution(top['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    top['moves'], len(top['moves']), visit_count
                )
            )
            break
        for direction in ('LEFT', 'DOWN', 'RIGHT', 'UP', ):
            moves_so_far = top['moves']
            if len(moves_so_far) > max_depth:
                max_depth = len(moves_so_far)
            nested_list = to_2d_list(top['state'])
            if can_move_blank(direction, nested_list):
                new_state = to_str(new_after_move(direction, nested_list))
                if new_state not in seen:
                    seen.add(new_state)
                    new_moves = moves_so_far[:]
                    new_moves.append(direction)
                    stack.append({'state': new_state, 'moves': new_moves})
                    # total = heuristic(new_state)
                    # pq.put( (total, {'state': new_state, 'moves': new_moves} ) )


# t0 = datetime.datetime.now()
#
# dfs(st_state, qu, saw)
#
# t1 = datetime.datetime.now()
#
# print((t1 - t0).total_seconds())

if len(sys.argv) != 3:
    print('Usage: eight_puzzle.py [search method] [initial state]')
else:
    st = sys.argv[2]
    st = st.replace(',', '')
    print(st)
    st_state = {'state': st, 'moves': []}
    if sys.argv[1] == 'bfs':
        bfs(st_state, qu, saw)
    elif sys.argv[1] == 'dfs':
        dfs(st_state, qu, saw)
    elif sys.argv[1] == 'astar':
        print('A* not implemented yet')
    print('max_depth:', max_depth)
    sys.getsizeof(st_state)
    sys.getsizeof(qu)
    sys.getsizeof(saw)
