from collections import defaultdict, namedtuple
'''
this code needed verification / testing
'''
MatchResult = namedtuple('MatchResult', ('winning_team', 'losing_team'))

def can_teamA_beat_teamB(matches, team_a, team_b):
    def build_graph():
        graph = defaultdict(set)
        for match in matches:
            graph[matches.winning_team].add(losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited = set()):
        if curr == dest: return True
        elif curr in visited or curr not in graph: return False
        else:
            visited.add(curr)
            for next_team in graph[curr]:
                if is_reachable_dfs(graph, next_team, dest): return True
            return False
