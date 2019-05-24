def march(i, ls):
    #print('ls')
    #print(ls)
    count = 0
    j = i
    i -= 1
    while i >=0 :
        if ls[i] == '.':
            i -= 1
        elif ls[i] == 'B':
            break
        elif ls[i] == 'p':
            count += 1
            break
    i = j + 1
    while i < len(ls):
        if ls[i] == '.':
            i += 1
        elif ls[i] == 'B':
            break
        elif ls[i] == 'p':
            count += 1
            break
    return count
            
        
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        num = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    #print('board[:][j]')
                    #print(board[:][j])
                    col = []
                    for y in range(8):
                        col.append(board[y][j])
                    #print('col')
                    #print(col)
                    row = [x for x in board[i][:]]
                    #print('row')
                    #print(row)
                    num = num + march(i, col)
                    #num = num + march(i, j, right)
                    #num = num + march(i, j, up)
                    num = num + march(j,  row)
                    
                    return num
                continue
        return num

        