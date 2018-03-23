import datetime
import sys

from eight_puzzle_helpers import is_solution, to_2d_list, to_str
from eight_puzzle_movers import can_move_blank, new_after_move


def bfs(queue, seen):
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


########################################################################################################################


def dfs(stack, seen):
    max_stack_size = -1
    max_seen_size = -1
    max_depth = -1
    visit_count = 0
    while stack:
        top = stack.pop()
        visit_count += 1
        stack_size = sys.getsizeof(stack)
        seen_size = sys.getsizeof(seen)
        if stack_size > max_stack_size:
            max_stack_size = stack_size
        if seen_size > max_seen_size:
            max_seen_size = seen_size
        if is_solution(top['state']):
            print(
                'Found solution {} of {} moves in {} visits'.format(
                    top['moves'], len(top['moves']), visit_count
                )
            )
            break
        for direction in ('UP', 'LEFT', 'DOWN', 'RIGHT'):
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

    return max_depth, max_stack_size, max_seen_size


########################################################################################################################


if len(sys.argv) == 1:
    start_state = {'state': '275318406', 'moves': []}
    seq = [start_state]
    seen_set = {start_state['state']}
    t0 = datetime.datetime.now()
    bfs(seq, seen_set)
    t1 = datetime.datetime.now()
    print('BFS in', (t1 - t0).total_seconds(), 'seconds')
    seq = [start_state]
    seen_set = {start_state['state']}
    t0 = datetime.datetime.now()
    result = dfs(seq, seen_set)
    t1 = datetime.datetime.now()
    print('DFS in', (t1 - t0).total_seconds(), 'seconds')
    print('max_depth:', result[0])
    print('max_stack_size:', result[1])
    print('max_seen_size:', result[2])
elif len(sys.argv) == 3:
    state = sys.argv[2]
    state = state.replace(',', '')
    start_state = {'state': state, 'moves': []}
    seq = [start_state]
    seen_set = {start_state['state']}
    if sys.argv[1] == 'bfs':
        t0 = datetime.datetime.now()
        bfs(seq, seen_set)
        t1 = datetime.datetime.now()
        print('BFS in', (t1 - t0).total_seconds(), 'seconds')
    elif sys.argv[1] == 'dfs':
        t0 = datetime.datetime.now()
        result = dfs(seq, seen_set)
        t1 = datetime.datetime.now()
        print('DFS in', (t1 - t0).total_seconds(), 'seconds')
        print('max_depth:', result[0])
        print('max_stack_size:', result[1])
        print('max_seen_size:', result[2])
    elif sys.argv[1] == 'astar':
        print('A* not implemented yet')
else:
    print('Usage: eight_puzzle.py [search method] [initial state]')
