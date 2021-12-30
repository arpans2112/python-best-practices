def isValidSudoku( board) -> bool:
    N = 9

    # Use an array to record the status
    # rows = [[0] * N for _ in range(N)]
    # cols = [[0] * N for _ in range(N)]
    # boxes = [[0] * N for _ in range(N)]

    # print(rows)
    # print(cols)
    # print(boxes)

    rows = [0] * N
    cols = [0] * N
    boxes = [0] * N

    for r in range(9):
        for c in range(9):

            if board[r][c] == '.':
                continue

            pos = int(board[r][c]) - 1

            if rows[r] & (1 << pos):
                return False
            else:
                rows[r] |= (1 << pos)

            if cols[c] & (1 << pos):
                return False
            else:
                cols[r] |= ( 1<<pos )

            idx = (r // 3) * 3 + (c // 3)

            if boxes[idx] & (1 << pos):
                return False
            boxes[idx] |= (1 << pos)

            # print(idx)

    for r in range(9):
        for c in range(9):

            idx = (r // 3) * 3 + (c // 3)
            # print(idx)
            # print(r, c, sep=":")










    # for r in board:
    #
    #     print(r)
    #     for c in range(N):
    #         # Check if the position is filled with number
    #         if board[r][c] == ".":
    #             continue
    #
    #         pos = int(board[r][c]) - 1
    #
    #         # Check the row
    #         if rows[r][pos] == 1:
    #             return False
    #         rows[r][pos] = 1
    #
    #         # Check the column
    #         if cols[c][pos] == 1:
    #             return False
    #         cols[c][pos] = 1
    #
    #         # Check the box
    #         idx = (r // 3) * 3 + c // 3
    #         if boxes[idx][pos] == 1:
    #             return False
    #         boxes[idx][pos] = 1
    #
    # return True


input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(input)