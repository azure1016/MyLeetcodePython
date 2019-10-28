
#        [    ['Bart',  'brother',   'Lisa'    ],
#            ['Bart',  'son',      'Homer'    ],
#            ['Marge', 'wife',     'Homer'    ],
#            ['Lisa',  'daughter', 'Homer'   ]    ]
#
#        i.e. inner lists have len == 3 and are in form name1, relationship, name2
#
# Given a series of relationships as a list of lists, and given two names, return
# all known "sequences" of relationships from name1 to name2
#
# e.g. with the lists above as input, with input names 'Bart' and 'Homer', you should return:
#    ['Bart son Homer', 'Bart brother Lisa daughter Homer']
#

from collections import defaultdict
class Relationship:
    def __init__(self, list_of_relationship):
        self.relationship = defaultdict(list)
        self.cord = defaultdict(defaultdict(list))
        self.dp = defaultdict(defaultdict)
        for name1, relation, name2 in list_of_relationship:
            self.relationship[name1].append((relation, name2))
            self.dp[name1][name2].append(name1 + " " + relation + " " + name2 + " ")
            self.cord[name1][name2].append(relation)



    def findRelation_dfs(self, name1, name2):
        runner = name1
        self.result = []
        self.dfs(name1, name2, name1 + " ", set(name1))
        return self.result
    # 这道题的DP好难，做不出来

    def dping(self, name1, name2):
        for name3 in self.cord[name1]:
            if not self.dp[name3][name2]:
                self.dping(name3, name2)
            for relation_chain in self.dp[name3][name2]:
                self.dp[name1][name2].append(name1 + " " + self.cord[name1][name3] + " " + relation_chain)



    def findRelation_dp(self, name1, name2):
        self.result_dp = []
        for name2 in self.dp[name1]:
            for name2 in self.dp[name1][name2]:
                self.dp[name1][name2] + " " + self.dping(name2, name3)
        return self.dp[name1][name2]

    def dfs(self, src, dst, cur_relation, names):
        if src not in self.relationship: return
        relatives = self.relationship[src]
        for (relation, name) in relatives:
            if name == dst: self.result.append(cur_relation + relation + " " + name)
            if name in names: continue
            new_names = set(names)
            new_names.add(src)
            self.dfs(name, dst, cur_relation + relation + " " + name + " ", new_names)

relations = [    ['Bart',  'brother',   'Lisa'    ],
           ['Bart',  'son',      'Homer'    ],
           ['Marge', 'wife',     'Homer'    ],
           ['Lisa',  'daughter', 'Homer'   ]    ]
relation_solver = Relationship(relations)
result = relation_solver.findRelation('Bart', 'Homer')
print(result)
