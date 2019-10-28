
from collections import deque, namedtuple
def findChildren(parent, d):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  children = set() # convenient for searching
  for i,ch in enumerate(parent):
    for a in alphabet:
      child = parent[:i]+a+parent[i+1:]
      if child == parent: continue
      #print("child:", child)
      if child in d:
        children.add(child)
  return children

def BFS(beginWord, endWord, d):
  d = set(d) # hashset
  # will there be rings in the graph, let's see
  q = deque()
  children, path, visited = 0, 1, 2
  q.append([set(), [beginWord], set([beginWord])]) # "children, path, visited"
  result = []
  while len(q) > 0:
    parent = q.popleft() # poll()?
    # print(parent)
    path_end = parent[1][-1]
    if path_end == endWord and (not result or len(parent[path]) <= len(result[-1])): 
        result.append(parent[path])
        continue
    parent[children] = findChildren(parent[path][-1], d)

    for child in parent[children]:
      if child not in parent[visited]:
        child_visited = set(parent[visited])
        child_visited.add(child)
        q.append([set(), parent[path] + [child], child_visited])
  return result
    
  
def test(beginWord, endWord, d):
  result = BFS(beginWord, endWord, d)
  if result:
    print("length of sequence:{}, the sequences:{}".format(len(result[0]), result))
  else:
    print("no way!")
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
test(beginWord, endWord, wordList)

'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation 
sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
  
  
  
  
  

      
      
      
      
      
      
      
      