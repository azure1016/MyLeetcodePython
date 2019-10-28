from bisect import *
class Planner:
    def closestStore(self, houses, stores):
        stores.sort()
        result = []
        n = len(stores)
        for house in houses:
            index = bisect_left(stores, house)
            if index == -1: 
                result.append(stores[index + 1])
                continue
            elif index == n:
                result.append(stores[index - 1])
            elif index == 0: result.append(stores[index])
            elif index in range(1, n):
                if abs(stores[index] - house) < abs(stores[index - 1] - house):
                    result.append(stores[index])
                else: result.append(stores[index - 1])
        return result

    def test(self, houses, stores):
        print(self.closestStore(houses, stores))
        print("------------")

sol = Planner()
houses1 = [5, 10, 17]
stores1 = [1, 5, 20, 11, 16]
sol.test(houses1, stores1)

houses2 = [2, 4, 2]
stores2 = [5, 1, 2, 3]
sol.test(houses2, stores2)

houses3 = [4, 8, 1, 1]
stores3 = [5, 3, 1, 2, 6]
sol.test(houses3, stores3)
