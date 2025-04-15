import time
import random
import os

# 游戏设置
WIDTH = 10
HEIGHT = 20

# 方块定义（只用 2 个简单的形状）
SHAPES = [
    [[1, 1, 1, 1]],       # I 形
    [[1, 1], [1, 1]],     # O 形
]

def create_board():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(''.join('█' if cell else ' ' for cell in row))
    print('-' * WIDTH)

def can_move(board, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if y + i >= HEIGHT or x + j < 0 or x + j >= WIDTH or board[y + i][x + j]:
                    return False
    return True

def place_shape(board, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                board[y + i][x + j] = 1

def clear_lines(board):
    new_board = [row for row in board if not all(row)]
    lines_cleared = HEIGHT - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [0 for _ in range(WIDTH)])
    return new_board, lines_cleared

def drop_shape(board, shape):
    x = WIDTH // 2 - len(shape[0]) // 2
    y = 0
    while can_move(board, shape, x, y + 1):
        y += 1
        print_board_with_shape(board, shape, x, y)
        time.sleep(0.1)
    place_shape(board, shape, x, y)
    return clear_lines(board)

def print_board_with_shape(board, shape, x, y):
    temp_board = [row[:] for row in board]
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and 0 <= y + i < HEIGHT and 0 <= x + j < WIDTH:
                temp_board[y + i][x + j] = 1
    print_board(temp_board)

def main():
    board = create_board()
    score = 0

    try:
        while True:
            shape = random.choice(SHAPES)
            board, lines = drop_shape(board, shape)
            score += lines
            print_board(board)
            print(f"得分: {score}")
            time.sleep(0.5)

            # 游戏结束条件
            if any(board[0]):
                print("游戏结束！")
                break
    except KeyboardInterrupt:
        print("\n退出游戏。")

if __name__ == "__main__":
    main()
