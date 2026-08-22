class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = [set() for _ in range(9)]   # rows[r]  = digits in row r
        cols  = [set() for _ in range(9)]   # cols[c]  = digits in column c
        boxes = [set() for _ in range(9)]   # boxes[b] = digits in box b

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":              # empty cell — skip
                    continue

                b = (r // 3) * 3 + (c // 3)  # which 3x3 box this cell is in

                # if the digit is ALREADY in this row, column, or box → duplicate
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                # otherwise, record it in all three
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        return True   # scanned everything, no duplicates found