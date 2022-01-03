class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedByAllOnes = self.trustedByAll(trust, n)
        trustNoOne = self.trustNoOne(trust, trustedByAllOnes)
        return trustNoOne if trustNoOne != None else -1
    
    def trustedByAll(self, trust, n):
        trusted = [0] * (n + 1)
        for relation in trust:
            a, b = relation[0], relation[1]
            if a != b:
                trusted[b] += 1
        
        return [i for i in range(1, n+1) if trusted[i] == n-1]
    
    def trustNoOne(self, trust, candidates):
        found = True
        for c in candidates:
            for relation in trust:
                if relation[0] == c:
                    found = False
                    break
                    
            if found:
                return c
        return None