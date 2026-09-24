class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for r in range(9):
            for c in range(9):
                x = board[r][c]

                if x == ".":
                    continue
                
                if (x in row[r] or x in col[c] or x in square[(r // 3, c // 3)]):
                    return False
                
                row[r].append(x)
                col[c].append(x)
                square[(r // 3, c // 3)].append(x)
        return True

