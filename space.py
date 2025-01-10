import curses
import time
from random import choice

ALIEN_ROWS = 3
ALIEN_COLS = 8
ALIEN_MOVE_DELAY = 0.5
BULLET_SPEED = 0.1

def draw_border(screen):
    h, w = screen.getmaxyx()
    for x in range(w):
        screen.addch(0, x, "-")
        screen.addch(h - 1, x, "-")
    for y in range(h):
        screen.addch(y, 0, "|")
        screen.addch(y, w - 1, "|")

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    screen.timeout(50)

    h, w = screen.getmaxyx()
    player_x = w // 2
    player_y = h - 2
    aliens = [[(2 + i * 2, 2 + j) for j in range(ALIEN_COLS)] for i in range(ALIEN_ROWS)]
    bullets = []
    alien_direction = 1
    last_alien_move = time.time()

    while True:
        screen.clear()
        draw_border(screen)

        screen.addch(player_y, player_x, "A")

        for row in aliens:
            for x, y in row:
                screen.addch(y, x, "X")

        for bx, by in bullets:
            screen.addch(by, bx, "|")

        bullets = [(x, y - 1) for x, y in bullets if y > 1]

        new_aliens = []
        for row in aliens:
            new_row = []
            for x, y in row:
                if (x, y) not in bullets:
                    new_row.append((x, y))
            if new_row:
                new_aliens.append(new_row)
        aliens = new_aliens

        if not aliens:
            screen.addstr(h // 2, w // 2 - 5, "YOU WIN!")
            screen.refresh()
            time.sleep(2)
            break

        if time.time() - last_alien_move > ALIEN_MOVE_DELAY:
            last_alien_move = time.time()
            max_x = max(max(x for x, y in row) for row in aliens)
            min_x = min(min(x for x, y in row) for row in aliens)
            if alien_direction == 1 and max_x >= w - 2:
                alien_direction = -1
                aliens = [[(x, y + 1) for x, y in row] for row in aliens]
            elif alien_direction == -1 and min_x <= 1:
                alien_direction = 1
                aliens = [[(x, y + 1) for x, y in row] for row in aliens]
            else:
                aliens = [[(x + alien_direction, y) for x, y in row] for row in aliens]

        if any(y >= player_y for row in aliens for x, y in row):
            screen.addstr(h // 2, w // 2 - 5, "GAME OVER!")
            screen.refresh()
            time.sleep(2)
            break

        key = screen.getch()
        if key == curses.KEY_LEFT and player_x > 1:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < w - 2:
            player_x += 1
        elif key == ord(" ") and len(bullets) < 3:
            bullets.append((player_x, player_y - 1))

        screen.refresh()
        time.sleep(0.05)

curses.wrapper(main)
