
def checkmate(board):

    rows_str = [line.strip() for line in board.strip().splitlines()]
    rows = [list(row) for row in rows_str]
    print(rows)

    if len(rows) != len(rows[0]):
        print("This board is not a square.")
        return
    
    king = 0
    ischeck = False

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if len(rows) != len(rows[j]):
                print(f"This board is not a square.")
                return
            
            if rows[i][j] != "P" and rows[i][j] != "B" and rows[i][j] != "R" and rows[i][j] != "Q" and rows[i][j] != "." and rows[i][j] != "K":
                print(f"{i}, {j}, {rows[i][j]}")
                print("This board format is wrong.")
                return
            else:
                if rows[i][j] == "P":
                    ischeck = ischeck or checkP(i, j, rows)
                if rows[i][j] == "B":
                    ischeck = ischeck or checkB(i, j, rows)
                if rows[i][j] == "R":
                    ischeck = ischeck or checkR(i, j, rows)
                if rows[i][j] == "Q":
                    ischeck = ischeck or checkQ(i, j, rows)

            if rows[i][j] == "K":
                king += 1
                if (king > 1):
                    print("There is more than 1 king.")
                    return
    if ischeck:
        print("Success")
    else:
        print("Fail")
            
def checkP(row, col, board):
    if (row -1 >= 0 
        and col - 1 >= 0 
        and board[row-1][col-1] == "K"):
        return True

    elif (row - 1 >= 0
        and col + 1 < len(board[row]) 
        and board[row - 1][col + 1] == "K"):
        return True
    
    return False

def checkB(row, col, board):
    #directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    b_len = len(board)
    

    #index rows-1, col-1
    r1 = row - 1
    c1 = col - 1
    while r1 >= 0 and c1 >= 0:
        if board[r1][c1] == "K":
            return True

        elif board[r1][c1] != ".":
            break
        
        r1 = r1 -1
        c1 = c1 - 1
        
    #index rows+1, col+1
    r2 = row + 1
    c2 = col + 1
    while r2 < b_len and c2 < b_len:
        if board[r2][c2] == "K":
            return True

        elif board[r2][c2] != ".":
            break
        
        r2 = r2 + 1
        c2 = c2 + 1
    
    #index rows+1, col-1
    r3 = row + 1
    c3 = col - 1
    while r3 < b_len and c3 >= 0:
        if board[r3][c3] == "K":
            return True

        elif board[r3][c3] != ".":
            break
    
        r3 = r3 + 1
        c3 = c3 - 1

    #index rows-1, col+1
    r4 = row - 1
    c4 = col + 1
    while r4 >= 0 and c4 < b_len:
        if board[r4][c4] == "K":
            return True

        elif board[r4][c4] != ".":
            break
    
        r4 = r4 - 1
        c4 = c4 + 1
    
    return False

def checkR(row, col, board):
    b_len = len(board)

    #vertical
    r1 = row - 1
    r2 = row + 1
    while r1 >= 0 or r2 < b_len :
        #lower
        if r1 >= 0:
            if board[r1][col] == "K":
                return True
            
            elif board[r1][col] != ".":
                r1 = -1

        #upper
        if r2 < b_len:
            if board[r2][col] == "K":
                return True
            elif board[r2][col] != ".":
                r2 = b_len
        
        r1 -= 1
        r2 += 1
    
    #horizonal
    c1 = col - 1
    c2 = col + 1
    while c1 >= 0 or c2 < b_len :
        #left
        if c1 >= 0:
            if board[row][c1] == "K":
                return True
            
            elif board[row][c1] != ".":
                c1 = -1

        #right
        if c2 < b_len:
            if board[row][c2] == "K":
                return True
            elif board[row][c2] != ".":
                c2 = b_len
        
        c1 -= 1
        c2 += 1
    
            
    return False

def checkQ(row, col, board):
    return checkB(row, col, board) or checkR(row, col, board)

    