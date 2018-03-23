import datetime

from eight_puzzle_helpers import goal
from eight_puzzle_movers import can_move_blank, new_after_move, heuristic


first_state = input('please enter initial state:')
first_state = first_state.replace(',','')
st_state = {'state': first_state, 'path_to_goal': []}
qu = [st_state]
saw = {st_state['state']}
Search_met= input('Please Select search method (bfs, dfs, ast):')

if Search_met == 'bfs':
 def bfs(st_state,queue, seen):
     cost_of_path = 0
     while queue:
         head,queue = queue[0], queue[1:]
         cost_of_path += 1
         if goal(head['state']):
             print(
                 'Path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nmax_search_depth:{}'.format(head['path_to_goal'], len(head['path_to_goal']), cost_of_path-1, len(head['path_to_goal']), len(head['path_to_goal'])+1))
             break
         for direction in ('UP', 'DOWN', 'LEFT', 'RIGHT'):
             moves_so_far = head['path_to_goal']
             # nested_list = twoDlist(head['state'])
             nested_list = head['state']
             if can_move_blank(direction, nested_list):
                 new_state = new_after_move(direction, nested_list)
                 if new_state not in seen:
                     seen.add(new_state)
                     new_moves = moves_so_far[:]
                     new_moves.append(direction)
                     queue.append({'state': new_state, 'path_to_goal': new_moves})

 t0 = datetime.datetime.now()

 bfs(st_state, qu, saw)

 t1 = datetime.datetime.now()

 print('running_time:',(t1 - t0).total_seconds())

elif Search_met == 'dfs':


 def dfs(st_state, queue, seen):
     global max_search_depth
#     visit_count = 0
     max_search_depth = -1
     cost_of_path = 0
     while queue:
         top = queue.pop()
         cost_of_path += 1
         if goal(top['state']):
             print('Path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nMax_search_depth: {}'.format(top['path_to_goal'], len(top['path_to_goal']), cost_of_path-1,len(top['path_to_goal']),max_search_depth+1))
             break
         for direction in ('RIGHT', 'LEFT', 'DOWN', 'UP'):
             moves_so_far = top['path_to_goal']
             if len(moves_so_far) > max_search_depth:
                 max_search_depth = len(moves_so_far)
             nested_list = top['state']
             if can_move_blank(direction, nested_list):
                 new_state = new_after_move(direction, nested_list)
                 if new_state not in seen:
                     seen.add(new_state)
                     new_moves = moves_so_far[:]
                     new_moves.append(direction)
                     queue.append({'state': new_state, 'path_to_goal': new_moves})


 t0 = datetime.datetime.now()

 dfs(st_state, qu, saw)

 t1 = datetime.datetime.now()

 print('running_time:',(t1 - t0).total_seconds())

elif Search_met == 'ast':

 def ast(queue, seen):
     global max_search_depth
     max_search_depth = -1
     cost_of_path = 0
     while queue:
         result_tuple = queue.get()  # (priority, state, moves)
         top = {'state': result_tuple[1], 'path_to_goal': result_tuple[2]}
         cost_of_path += 1
         if goal(top['state']):
             print(
                 'Path_to_goal: {}\ncost_of_path: {}\nnodes_expanded: {}\nsearch_depth: {}\nMax_search_depth: {}'.format(
                     top['path_to_goal'], len(top['path_to_goal']), cost_of_path - 1, len(top['path_to_goal']),
                     max_search_depth + 1))
             break
         for direction in ('RIGHT', 'LEFT', 'DOWN', 'UP'):
             moves_so_far = top['path_to_goal']
             if len(moves_so_far) > max_search_depth:
                 max_search_depth = len(moves_so_far)
             nested_list = top['state']
             if can_move_blank(direction, nested_list):
                 new_state = new_after_move(direction, nested_list)
                 print(new_state)
                 if new_state not in seen:
                     seen.add(new_state)
                     new_moves = moves_so_far[:]
                     new_moves.append(direction)
                     #queue.append({'state': new_state, 'path_to_goal': new_moves})
                     g = ...
                     h = heuristic(new_state)
                     queue.put( (g + h, new_state, new_moves) )

 t0 = datetime.datetime.now()

 # priority_queue = [st_state]
 from queue import PriorityQueue
 priority_queue = PriorityQueue()
 priority = heuristic(st_state['state'])
 state = st_state['state']
 moves = []
 priority_queue.put( (priority, state, moves) )
 ast(priority_queue, saw)

 t1 = datetime.datetime.now()

 print('running_time:', (t1 - t0).total_seconds())
