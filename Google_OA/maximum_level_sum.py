from collections import deque, namedtuple
import sys
from lc_util import Tree

Node = namedtuple('Node', "node, level")
class MyTree:
    def maxLevelSum(self, root):
        '''
        :param root: level is 1
        :return: the level having the max level sum
        '''
        root_node = Node(root, 1)
        queue = deque()
        queue.append(root_node)
        LevelSum = namedtuple('LevelSum', "level, sum")
        result = LevelSum(1, -sys.maxsize)
        while len(queue):
            sum_ = 0
            cur_level = -1
            for i in range(len(queue)):
                cur = queue.popleft()
                cur_level = cur.level
                sum_ += cur.node.val
                if cur.node.left:
                    queue.append(Node(cur.node.left, cur.level + 1))
                if cur.node.right:
                    queue.append(Node(cur.node.right, cur.level + 1))
            if sum_ > result.sum:
                result = LevelSum(cur_level, sum_)
        return result.level

    def test1(self):
        tree = [7, 3, 2,None, 4,None,4,2,1,5]
        root = Tree(tree)
        res = self.maxLevelSum(root)
        print(res)



