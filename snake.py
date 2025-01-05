import curses
import random

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.nodelay(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    height, width = 20, 50
    win = curses.newwin(height, width, 0, 0)
    win.border(0)
    win.timeout(100)

    snake = [[10, 25], [10, 24], [10, 23]]
    food = [random.randint(1, height - 2), random.randint(1, width - 2)]
    win.addch(food[0], food[1], curses.color_pair(2) + ord("O"))

    direction = curses.KEY_RIGHT
    score = 0

    while True:
        win.addstr(0, 2, f"Score: {score} ", curses.color_pair(3))

        next_key = win.getch()
        direction = next_key if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT] else direction

        head = snake[0]
        if direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]

        if (
            new_head in snake
            or new_head[0] == 0  
            or new_head[0] == height - 1 
            or new_head[1] == 0  
            or new_head[1] == width - 1
        ):
            win.addstr(height // 2, width // 2 - 5, "GAME OVER!", curses.color_pair(2))
            win.refresh()
            curses.napms(2000)
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = [random.randint(1, height - 2), random.randint(1, width - 2)]
            win.addch(food[0], food[1], curses.color_pair(2) + ord("O"))
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], " ")

        for segment in snake:
            win.addch(segment[0], segment[1], curses.color_pair(1) + ord("#"))

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Game exited.")
