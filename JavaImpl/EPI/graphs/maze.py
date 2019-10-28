WHITE, BLACK = 1, 0
'''
not tested
'''
def search_maze(maze, s, e):
    path = []
    def search_maze_helper(cur):
        if cur[0] not in range(0, len(maze)) or cur[1] not in range(0, len(maze[0])) or maze[cur[0]][cur[1]] == BLACK:
            return False
        
        path.append(cur)
        maze[cur[0]][cur[1]] = BLACK # not visiting it again
        if cur == e: return True
        if any(map(search_maze_helper, [(cur[0]+1, cur[1]), (cur[0]-1, cur[1]), (cur[0], cur[1]+1), (cur[0], cur[1]-1)])):
            return True
        else:
            del path[-1]
            return False
    
    if not search_maze_helper(s): return []
    else: return path
