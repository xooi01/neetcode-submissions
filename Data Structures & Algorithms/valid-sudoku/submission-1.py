class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            digits = [r for r in row if r.isdigit()]
            if len(digits) != len(set(digits)):
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
                    


        