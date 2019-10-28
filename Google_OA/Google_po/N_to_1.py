import json
class Calculator:
    def N_to_1(self, n):
        cache = {1:0, 2:1}
        for i in range(3, n+1):
            step = 0
            if i in cache:
                continue
            else:
                became = i
                while True:
                    became = self.transform(became)
                    step += 1
                    if became in cache:
                        cache[i] = cache[became] + step
                        break
        return cache
                        

    def transform(self, n):
        if n % 2: return n * 3 + 1
        else: return n // 2

    def solve(self, n):
        cache = self.N_to_1(n)
        print(json.dumps(cache, indent = 2))
        peak = max(cache.values())
        print([key for key, val in cache.items() if val == peak])

sol = Calculator()
sol.solve(40)
