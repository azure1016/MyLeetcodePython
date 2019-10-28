class Watering:
    def water(self, plants, capacity):
        steps = 0
        remained = capacity
        for i, p in enumerate(plants):
            if remained < p:
                steps += i * 2
                remained = capacity - p
            else:
                remained -= p
        steps += len(plants)
        return steps

    def findSteps(self, plants, capacity):
        can = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] <= can:
                steps += 1
                can -= plants[i]
            else:
                steps += 2 * i + 1
                can = capacity - plants[i]
        return steps

sol = Watering()
plants = [2,4,5,1,3,4,5,2,1,6,5]
cap = 6
res = sol.water(plants, cap)
res_of_others = sol.findSteps(plants, cap)
print(res == res_of_others)