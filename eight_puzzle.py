from eight_puzzle_helpers import *
from eight_puzzle_movers import *

start_state = {'state': '275318406', 'moves': []}
queue = [start_state]
seen = {start_state['state']}

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

bfs(start_state, queue, seen)
