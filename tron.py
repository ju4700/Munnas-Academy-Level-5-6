import curses
import time

def draw_grid(stdscr, grid, score1, score2):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                stdscr.addch(y, x, grid[y][x])

    score_text = f"Player 1: {score1} | Player 2: {score2}"
    stdscr.addstr(0, w // 2 - len(score_text) // 2, score_text)

    stdscr.refresh()

def tron_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    h, w = stdscr.getmaxyx()

    grid = [[0 for _ in range(w)] for _ in range(h)]

    player1 = [h // 2, w // 4]
    player2 = [h // 2, 3 * w // 4]
    direction1 = [0, 1]  
    direction2 = [0, -1]  

    symbol1 = '1'
    symbol2 = '2'

    score1, score2 = 0, 0

    while True:
        key = stdscr.getch()

        if key == ord('w') and direction1 != [1, 0]:
            direction1 = [-1, 0]
        elif key == ord('s') and direction1 != [-1, 0]:
            direction1 = [1, 0]
        elif key == ord('a') and direction1 != [0, 1]:
            direction1 = [0, -1]
        elif key == ord('d') and direction1 != [0, -1]:
            direction1 = [0, 1]

        if key == curses.KEY_UP and direction2 != [1, 0]:
            direction2 = [-1, 0]
        elif key == curses.KEY_DOWN and direction2 != [-1, 0]:
            direction2 = [1, 0]
        elif key == curses.KEY_LEFT and direction2 != [0, 1]:
            direction2 = [0, -1]
        elif key == curses.KEY_RIGHT and direction2 != [0, -1]:
            direction2 = [0, 1]

        player1[0] += direction1[0]
        player1[1] += direction1[1]
        player2[0] += direction2[0]
        player2[1] += direction2[1]

        if (player1[0] < 0 or player1[0] >= h or
            player1[1] < 0 or player1[1] >= w or
            grid[player1[0]][player1[1]] != 0):
            score2 += 1
            break

        if (player2[0] < 0 or player2[0] >= h or
            player2[1] < 0 or player2[1] >= w or
            grid[player2[0]][player2[1]] != 0):
            score1 += 1
            break

        grid[player1[0]][player1[1]] = symbol1
        grid[player2[0]][player2[1]] = symbol2

        draw_grid(stdscr, grid, score1, score2)

    return score1, score2

def main():
    curses.wrapper(tron_game)

if __name__ == "__main__":
    main()