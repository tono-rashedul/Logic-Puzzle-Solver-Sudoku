import pygame
from constants import *
from solver import constraint_propagation, is_valid

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))  # Extend window height to fit button
pygame.display.set_caption("Sudoku Solver")
FONT = pygame.font.SysFont('arial', 40)
BUTTON_FONT = pygame.font.SysFont('arial', 20)

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

selected_cell = None  # To store the selected cell (row, column)


def draw_grid():
    for i in range(GRID_SIZE + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), thickness)


def draw_numbers():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                value = FONT.render(str(board[i][j]), True, BLACK)
                screen.blit(value, (j * SQUARE_SIZE + 15, i * SQUARE_SIZE + 10))


def draw_selection():
    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)


def handle_click(pos):
    global selected_cell
    x, y = pos
    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
    selected_cell = (row, col)


def handle_input(key):
    if selected_cell:
        row, col = selected_cell
    else:
        return

    if key in range(pygame.K_1, pygame.K_9 + 1):  # Check if key is 1-9
        num = key - pygame.K_0
        if is_valid(board, num, (row, col)):
            board[row][col] = num


def solve_with_ai():
    """
    Solve the puzzle using Constraint Propagation AI solver.
    """
    if constraint_propagation(board):
        print('Solved using Constraint Propagation!')
    else:
        print('Could not solve the puzzle.')


def main():
    global selected_cell
    running = True

    # Define Solve Button: centered horizontally, positioned slightly below the grid
    button_width = 200
    button_height = 40
    solve_button = pygame.Rect((WIDTH - button_width) // 2, HEIGHT + 10, button_width, button_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.collidepoint(event.pos):
                    solve_with_ai()  # Call AI solver
                else:
                    handle_click(event.pos)

            elif event.type == pygame.KEYDOWN:
                handle_input(event.key)

        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        draw_selection()

        # Draw the Solve with AI Button
        pygame.draw.rect(screen, GRAY, solve_button)

        # Center the text within the button
        solve_text = BUTTON_FONT.render('Solve with AI', True, BLACK)
        text_x = solve_button.x + (button_width - solve_text.get_width()) // 2
        text_y = solve_button.y + (button_height - solve_text.get_height()) // 2
        screen.blit(solve_text, (text_x, text_y))  # Centered text

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
