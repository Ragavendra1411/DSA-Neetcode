class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        inner_squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]==".":
                    continue
                if board[row][col] in rows[row]:
                    return False
                else:
                    rows[row].add(board[row][col])
                if board[row][col] in cols[col]:
                    return False
                else:
                    cols[col].add(board[row][col])
                if board[row][col] in inner_squares[(row//3,col//3)]:
                    return False
                else:
                    inner_squares[(row//3,col//3)].add(board[row][col])

        return True
                    


