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
