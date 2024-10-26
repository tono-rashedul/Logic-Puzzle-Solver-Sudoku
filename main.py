import pygame

from constants import *
from solver import solve, is_valid

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
FONT = pygame.font.SysFont('arial', 40)

# Initial Sudoku board (0 means empty)
board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

selected_cell = None  # to store the selected cell (rows colum)


def draw_grid():
    # Draw the Sudoku grid.
    for i in range(GRID_SIZE + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), thickness)


def draw_numbers():
    # Draw numbers on the board.
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                value = FONT.render(str(board[i][j]), True, BLACK)
                screen.blit(value, (j * SQUARE_SIZE + 15, i * SQUARE_SIZE + 10))


def draw_selection():
    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(
            screen, BLUE,
            (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3
        )


def handle_click(pos):
    global selected_cell
    x, y = pos
    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
    selected_cell = (row, col)  # store the selected cell


def handle_input(key):
    if selected_cell:
        row, col = selected_cell
    else:
        return

    if key in range(pygame.K_1, pygame.K_9 + 1):  # check if is 1-9
        num = key - pygame.K_0
        if is_valid(board, num, (row, col)):
            board[row][col] = num


def check_win():
    if solve(board):
        print('Winner!')
    else:
        print('Better luck next time!')


def main():
    # Main game loop.
    global selected_cell
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    check_win()
                else:
                    handle_input(event.key)

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        draw_selection()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
