class Solution:
    # a TLE solution. Use integer counters instead
    def gridIllumination(self, N, lamps, queries):
        # step 1: initialize
        land = self.light_land(lamps, N)
        valid_lamps = 0
        # step 2: process queries and turn of lamps
        for x, y in queries:
            col_setter = 1 << (N - y - 1)
            if not (land[x] & col_setter):  # if cell[x,y] is off
                return [x, y]

            # turn off the lights if adjacent
            # same row: land[x] & (col_setter << 1), land[x] & (col_setter >> 1)
            # same col: land[x+1] & col_setter, land[x-1] & col_setter

            for i, (r, c) in enumerate(lamps):
                for p, q in [(1, 0), (1, 1), (1, -1), (0, 1), (0, 0), (-1, 0), (-1, 1), (-1, -1), (0, -1)]:
                    if x + p == r and y + q == c:
                        # turn off r,c, valid_lamp += 1
                        # valid_lamps += 1
                        lamps[i] = [-1, -1]
            land = self.light_land(lamps, N)  # reset according to updated on- lamps


    def light_land(self, lamps, N):
        mask = (1 << N) - 1
        land = [0 for _ in range(N)]  # initially all are off
        for x, y in lamps:  # N * m
            if x == -1 and y == -1:
                continue
            land[x] |= mask  # set the whole row to 1
            col_setter = 1 << (N - y- 1)
            for i in range(N):
                land[i] |= col_setter
            # set diagonals to 1
            col_setter1 = col_setter2 = col_setter
            for i in reversed(range(x)):
                land[i] |= col_setter1 >> 1 | col_setter2 << 1
                land[i] &= mask
                col_setter1 >>= 1
                col_setter2 <<= 1
            col_setter1 = col_setter2 = col_setter
            for i in range(x+1, N):
                land[i] |= col_setter1 >> 1 | col_setter2 << 1
                land[i] &= mask
                col_setter1 >>= 1
                col_setter2 <<= 1
        return land


N = 5
lamps = [[0,0], [1,3], [4,4]]
queries = [[1,1], [1,0]]
sl = Solution()
res = sl.gridIllumination(N, lamps, queries)
print(res)








