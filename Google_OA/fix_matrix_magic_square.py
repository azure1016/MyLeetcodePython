class MagicSquare:
    def fillMatrix(self, n):
        if n % 2 == 0: return None
        square = [[0 for _ in range(n)] for _ in range(n)]
        row = n // 2
        col = n - 1
        num = 1
        while num <= n ** 2:
            if row == -1 and col == n:
                row, col = 0, n-2
            if square[(row + n) % n][(col+n) % n]:
                row, col = row + 1, col - 2
                continue
            square[(row + n) % n][(col + n) % n] = num
            num += 1
            row = (row + n) % n
            row -= 1
            col = (col + n) % n
            col += 1
        return square

    def printResult(self, square):
        n = len(square)
        sum_of_line = []
        for i in range(n):
            line = []
            for j in range(n):
                line.append(square[i][j])
            print(" ".join([str(num) for num in line]))
            sum_of_line.append(sum(line))
        print(" ".join([str(sum_) for sum_ in sum_of_line]))

sol = MagicSquare()
sq3 = sol.fillMatrix(3)
sol.printResult(sq3)

print("-----------------------------")
print("-----------------------------")

sq4 = sol.fillMatrix(5)
sol.printResult(sq4)
            
