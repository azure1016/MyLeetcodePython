class Flipper:
    def __init__(self):
        pass

    # sliding window would also work
    def flip(self, lights):
        intervals = [[0,-1,0]]
        turned = 0
        for i in range(len(lights)):
            if lights[i] ^ turned: # if i = 0, turned = 1, then should change turned; else if i = 1, turned = 1,should not
                turned ^= 1
                intervals.append([i, i, 1])
                continue
            intervals[-1][1] += 1
            intervals[-1][2] += 1
        maximum = intervals[0]
        for i in range(len(intervals) - 2):
            sum_3 = intervals[i][2] + intervals[i+1][2] + intervals[i+2][2]
            if sum_3 > maximum[2]:
                maximum = [intervals[i][0], intervals[i+2][1], sum_3]
        return [maximum[0], maximum[1]]




    def flip_wrong(self, lights): # 1 for red, 0 for green
        red_count = lights[0]
        green_count = (lights[0] + 1) % 2
        max_record = [0, 0, 0] # i, j , max_length
        for i in range(1, len(lights)):
            if lights[i] ^ lights[i-1]: # color changed
                if max_record[2] < red_count + green_count:
                    max_record[2] = red_count + green_count
                    if lights[i]: # it turned red
                        max_record[0] = i - green_count
                        red_count = 0
                    else: # it turned green
                        max_record[0] = i - red_count
                        green_count = 0
                    max_record[1] = i-1
            green_count += (lights[i] + 1) % 2
            red_count += lights[i]
        return [max_record[1] - max_record[2], max_record[1]]


flipper = Flipper()
lights = [0,1,1,0,0,0,1,0,1,1,1,0,0,0,1]
res = flipper.flip(lights)
print(res)