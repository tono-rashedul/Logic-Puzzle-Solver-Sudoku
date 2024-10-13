import pygame

from constants import *
from solver import solve

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
FONT = pygame.font.SysFont('arial', 40)

# Initial Sudoku board (0 means empty)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


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


def main():
    # Main game loop.
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(board)

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
