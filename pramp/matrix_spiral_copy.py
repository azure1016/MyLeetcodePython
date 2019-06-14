def spiral_copy(arr):
    width = len(arr[0])
    height = len(arr)
    start_row, start_column = 0, 0
    result = []
    while width >= 1 and height >= 1:
        for rightward in range(start_column, start_column + width):
            result.append(arr[start_row][rightward])
        if height > 1:
            for downward in range(start_row + 1, start_row + height - 1):
                result.append(arr[downward][start_column + width - 1])

            for leftward in range(start_column + width - 1, start_column - 1, -1):
                result.append(arr[start_row + height - 1][leftward])

            for upward in range(start_row + height - 2, start_row, -1):
                result.append(arr[upward][start_column])
        start_row += 1
        start_column += 1
        width -= 2
        height -= 2
    return result

#test case:
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
result = spiral_copy(arr)
print(result)
'''
1 2 3 4 6
5 6 7 8 6
9 1 0 2 6
3 4 5 6 6
while width and height both <=1
first layer, start at 
the 0 th:(0,0),turn (0,len(arr[0]) - 1), turn (  len(arr) - 1, len(arr) - 1), ended at[0 + 1,0]
        stx,sty      (stx, sty+width - 1)     (stx+height-1, sty+width-1), ended at(stx+1,sty)
the 1 th:(1,1), turn(1, len(arr[0])-1-1),turn (len(arr[0])-1-1,len(arr)-1-1), ended at(len(arr[0]-1-1, 1)
  (stx1,sty1) (stx1,sty1+width1-1) (stx1+height1-1,sty1+width1-1) (stx1+1,sty)
'''
