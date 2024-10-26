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

    # Check the column
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


def solve(board):
    """
    Solves the board using the backtracking algorithm.
    :param board: 2D list representing the Sudoku board.
    :return: True if solvable, False otherwise.
    """
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            # Reset the position (backtrack)
            board[row][col] = 0

    return False


def find_empty(board):
    """
    Find an empty space in the board.
    :param board: The current board state.
    :return: Tuple (row, col) of empty position or None if full.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # Row, Col
    return None
