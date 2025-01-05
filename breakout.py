import curses
import time

PADDLE_WIDTH = 8
BALL_SYMBOL = 'O'
BLOCK_SYMBOL = 'X'
FRAME_DELAY = 0.05 

def draw_window(stdscr, paddle_x, ball, blocks, lives, score):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for x in range(paddle_x, paddle_x + PADDLE_WIDTH):
        stdscr.addch(h - 2, x, '=')

    stdscr.addch(ball[0], ball[1], BALL_SYMBOL)

    for block in blocks:
        stdscr.addch(block[0], block[1], BLOCK_SYMBOL)

    stdscr.addstr(0, 2, f"Lives: {lives}  Score: {score}")

    stdscr.refresh()

def breakout_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    h, w = stdscr.getmaxyx()

    paddle_x = w // 2 - PADDLE_WIDTH // 2

    ball = [h - 3, w // 2]
    ball_dir = [-1, 1] 

    blocks = [[y, x] for y in range(3, 8) for x in range(5, w - 5, 4)]

    lives = 3
    score = 0

    while lives > 0:
        key = stdscr.getch()

        if key == curses.KEY_LEFT and paddle_x > 0:
            paddle_x -= 2
        elif key == curses.KEY_RIGHT and paddle_x < w - PADDLE_WIDTH:
            paddle_x += 2

        ball[0] += ball_dir[0]
        ball[1] += ball_dir[1]

        if ball[1] <= 0 or ball[1] >= w - 1:
            ball_dir[1] *= -1  
        if ball[0] <= 0:
            ball_dir[0] *= -1  

        if ball[0] == h - 3 and paddle_x <= ball[1] < paddle_x + PADDLE_WIDTH:
            ball_dir[0] *= -1
            paddle_center = paddle_x + PADDLE_WIDTH // 2
            if ball[1] < paddle_center: 
                ball_dir[1] = -1
            elif ball[1] > paddle_center:  
                ball_dir[1] = 1

        for block in blocks:
            if ball == block:
                blocks.remove(block)
                ball_dir[0] *= -1
                score += 10
                break

        if ball[0] >= h - 1:
            lives -= 1
            ball = [h - 3, w // 2]  
            ball_dir = [-1, 1]  

        if not blocks:
            stdscr.addstr(h // 2, w // 2 - 5, "You Win!")
            stdscr.refresh()
            time.sleep(2)
            break

        draw_window(stdscr, paddle_x, ball, blocks, lives, score)
        time.sleep(FRAME_DELAY)

    if lives == 0:
        stdscr.addstr(h // 2, w // 2 - 5, "Game Over!")
        stdscr.refresh()
        time.sleep(2)

def main():
    curses.wrapper(breakout_game)

if __name__ == "__main__":
    main()