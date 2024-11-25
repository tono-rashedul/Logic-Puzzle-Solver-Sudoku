def is_valid(board, num, pos):
    """
        Check if the number is valid in the current position.
        :param board: The current board state.
        :param num: The number to place (1-9).
        :param pos: The tuple of (row, col) where the number is placed.
        :return: True if valid, False otherwise.
        """

    # Check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check The Column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check the 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # Row, Col
    return None


def solve(board):
    """
        Solves the board using the backtracking algorithm.
        :param board: 2D list representing the Sudoku board.
        :return: True if solvable, False otherwise.
    """
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0

    return False


def constraint_propagation(board):  # CSP
    def get_possibilities(board):
        possibilities = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} if board[i][j] == 0 else {board[i][j]}
                          for j in range(len(board[0]))] for i in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != 0:
                    num = board[row][col]
                    for i in range(len(board)):
                        if num in possibilities[row][i]:
                            possibilities[row][i].remove(num)
                        if num in possibilities[i][col]:
                            possibilities[i][col].remove(num)

                    box_x, box_y = col // 3, row // 3
                    for i in range(box_y * 3, box_y * 3 + 3):
                        for j in range(box_x * 3, box_x * 3 + 3):
                            if num in possibilities[i][j]:
                                possibilities[i][j].remove(num)
        return possibilities

    def fill_single_possibilities(board, possibilities):
        updated = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0 and len(possibilities[row][col]) == 1:
                    board[row][col] = possibilities[row][col].pop()
                    updated = True
        return updated

    possibilities = get_possibilities(board)
    while True:
        if fill_single_possibilities(board, possibilities):
            possibilities = get_possibilities(board)
        else:
            break

    if find_empty(board):
        return solve(board)
    return True
