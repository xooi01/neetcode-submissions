class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            rowDigits = [r for r in row if r.isdigit()]
            if len(rowDigits) != len(set(rowDigits)):
                return False

        # Check columns 
        for col_idx in range(len(row)):
            colVals = [board[r][col_idx] for r in range(9)]
            colDigits = [c for c in colVals if c.isdigit()]
            if len(colDigits) != len(set(colDigits)):
                return False
        
        # Check boxes
        for row_box in range(0, 9, 3):
            for col_box in range(0, 9, 3):
                boxDigits = []
                for r in range(3):
                    for c in range(3):
                        boxVals = board[row_box + r][col_box + c]
                        if boxVals.isdigit():
                            boxDigits.append(boxVals)
                if len(boxDigits) != len(set(boxDigits)):
                    return False
        return True
                    
# 21:06

        