class Solution:
    def flip (self, angle, is_clockwise, pic): #pic: N*N array-like
        i = int (angle / 90) % 4
        if i == 0:
            return pic
        if i == 1 and is_clockwise:
            return self.right_turn (pic)
        elif i == 1 and not is_clockwise:
            return self.left_turn (pic)
        elif i == 2:
            return self.upside_down (pic)
        elif i == 3 and is_clockwise:
            return self.left_turn (pic)
        elif i == 3 and not is_clockwise:
            return self.right_turn (pic)
    
    def left_turn (self, pic):
        N = len (pic) 
        newpic = []
        for i in range(0, N):
            row = []
            for j in range(0, N):
                row.append(pic[j][N - 1 - i])
            newpic.append(row)
        return newpic
    def right_turn(self, pic):
        N = len(pic)
        newpic = []
        for i in range(0, N):
            row = []
            for j in range(0, N):
                #pic[i][j], pic[j][i] = pic[j][i], pic[i][j]
                row.append(pic[N - 1 -j][i])
            newpic.append(row)
        return newpic

    def upside_down(self, pic):
        pic_1 = self.left_turn(pic)
        return self.left_turn(pic_1)

    def pr_arr(self, arr):
        for x in arr:
            print(x,'\n')

test = Solution()

arr =[['*',' ',' ','*'],
[' ',' ',' ',' '],
['*',' ',' ',' '],
['*','*','*','*']
]
print("arr:")
test.pr_arr(arr)

pic_right = test.flip(90, True, arr)

pic_left = test.flip(90, False, arr)

pic_right_ng = test.flip(-90, True, arr)

pic_up_down = test.flip(180, True, arr)

pic_up_d = test.flip(180, False, arr)

print('left turn:')
test.pr_arr(pic_left)
print('right turn:')
test.pr_arr(pic_right)
print('right on anti-clockwise:')
test.pr_arr(pic_right_ng)
print('upside down:')
test.pr_arr(pic_up_down)
print('upside down neg:')
test.pr_arr(pic_up_d)
