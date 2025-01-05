import curses
import time


def draw_window(stdscr, paddle1, paddle2, ball, score1, score2):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for y in paddle1:
        stdscr.addch(y, 2, '|')
    for y in paddle2:
        stdscr.addch(y, w - 3, '|')

    stdscr.addch(ball[0], ball[1], 'O')

    score_text = f"{score1} - {score2}"
    stdscr.addstr(0, w // 2 - len(score_text) // 2, score_text)

    stdscr.refresh()


def pong_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    h, w = stdscr.getmaxyx()
    paddle_height = 5

    paddle1 = [i for i in range(h // 2 - paddle_height // 2, h // 2 + paddle_height // 2)]
    paddle2 = [i for i in range(h // 2 - paddle_height // 2, h // 2 + paddle_height // 2)]

    ball = [h // 2, w // 2]
    ball_dir = [-1, -1]

    score1, score2 = 0, 0

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and paddle2[0] > 1:
            paddle2 = [y - 1 for y in paddle2]
        elif key == curses.KEY_DOWN and paddle2[-1] < h - 1:
            paddle2 = [y + 1 for y in paddle2]

        if key == ord('w') and paddle1[0] > 1:
            paddle1 = [y - 1 for y in paddle1]
        elif key == ord('s') and paddle1[-1] < h - 1:
            paddle1 = [y + 1 for y in paddle1]

        ball[0] += ball_dir[0]
        ball[1] += ball_dir[1]

        if ball[0] <= 0 or ball[0] >= h - 1:
            ball_dir[0] *= -1

        if ball[1] == 3 and ball[0] in paddle1:
            ball_dir[1] *= -1
        if ball[1] == w - 4 and ball[0] in paddle2:
            ball_dir[1] *= -1

        if ball[1] <= 0:
            score2 += 1
            ball = [h // 2, w // 2]
            ball_dir = [-1, -1]
        if ball[1] >= w - 1:
            score1 += 1
            ball = [h // 2, w // 2]
            ball_dir = [-1, 1]

        draw_window(stdscr, paddle1, paddle2, ball, score1, score2)


def main():
    curses.wrapper(pong_game)


if __name__ == "__main__":
    main()
