import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100) 

    height, width = stdscr.getmaxyx()
    trex_pos = [height - 3, 5] 
    obstacle_x = width - 1  

    score = 0
    is_jumping = False
    jump_count = 0

    while True:
        stdscr.clear()

        for x in range(width):
            stdscr.addstr(height - 2, x, "-")

        stdscr.addstr(trex_pos[0], trex_pos[1], "T")

        stdscr.addstr(height - 3, obstacle_x, "X")

        key = stdscr.getch()
        if key == ord("q"):
            break
        elif key == ord(" ") and not is_jumping:
            is_jumping = True

        if is_jumping:
            if jump_count < 5: 
                trex_pos[0] -= 1
            elif jump_count < 10: 
                trex_pos[0] += 1
            jump_count += 1
            if jump_count == 10:
                is_jumping = False
                jump_count = 0

        obstacle_x -= 1
        if obstacle_x < 0:
            obstacle_x = width - 1
            score += 1  
            
        if trex_pos[0] == height - 3 and trex_pos[1] == obstacle_x:
            stdscr.addstr(height // 2, width // 2 - 5, "GAME OVER!")
            stdscr.addstr(height // 2 + 1, width // 2 - 5, f"Score: {score}")
            stdscr.refresh()
            time.sleep(2)
            break

        stdscr.addstr(0, 0, f"Score: {score}")

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
 