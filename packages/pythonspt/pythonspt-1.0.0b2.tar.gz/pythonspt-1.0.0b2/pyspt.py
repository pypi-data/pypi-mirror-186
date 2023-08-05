import argparse
import curses
import threading
import time
from itertools import cycle
from os import system
from queue import Empty, Queue
from shutil import which

from constants import TIME_FORMAT, TIMER_HEIGHT, TIMER_TEXT, TIMER_WIDTH, TTY_CLOCK

parser = argparse.ArgumentParser(
    description="A simple terminal timer that uses the pomodoro technique.",
)
parser.add_argument(
    "-p",
    "--pomodoro",
    dest="pomodoro",
    type=int,
    default=25,
    help="Pomodoro duration in minutes (default: 25)",
)
parser.add_argument(
    "-sb",
    "--short-break",
    dest="short_break",
    type=int,
    default=5,
    help="Short break duration in minutes (default: 5)",
)
parser.add_argument(
    "-lb",
    "--long-break",
    dest="long_break",
    type=int,
    default=15,
    help="Long break duration in minutes (default: 15)",
)
parser.add_argument(
    "-lbi",
    "--long-break-interval",
    dest="long_break_interval",
    type=int,
    default=3,
    help="Long break interval (default: 3)",
)

args = parser.parse_args()
pomodoro_duration = args.pomodoro * 60
short_break_duration = args.short_break * 60
long_break_duration = args.long_break * 60

TIMER_DURATION = {
    "pomodoro": args.pomodoro * 60,
    "short_break": args.short_break * 60,
    "long_break": args.long_break * 60,
}


def draw_timer(stdscr, y_start, x_start, time_str):
    for row in range(5):  # Draw the timer row by row
        timer_row_str = ""
        for character in time_str:  # For each row, draw each part of the characters
            if (
                character == ":" and int(time_str[-1]) % 2 == 1
            ):  # Check if current seconds is odd or even
                timer_row_str += TTY_CLOCK[" "][row]  # For the blinking ":" effect
            else:
                timer_row_str += TTY_CLOCK[character][row]
            timer_row_str += " "
        stdscr.addstr(y_start + row, x_start, timer_row_str)


# def beep():
#     if which("powershell.exe"):
#         system("powershell.exe '[console]::beep(1450,800)'")


def get_midpoint(stdscr):
    height, width = stdscr.getmaxyx()
    y_mid = (height - 1) // 2
    x_mid = (width - 1) // 2

    return y_mid, x_mid


def get_timer_xy_coords(stdscr):
    y_mid, x_mid = get_midpoint(stdscr)
    y_start = (
        y_mid - TIMER_HEIGHT // 2
    )  # Length of timer is 5 rows high -> start printing ~2 cells above the middle
    x_start = (
        x_mid - TIMER_WIDTH // 2
    )  # Length of timer is 30 columns wide -> start printing 15 cells to the left of the middle

    return (y_start, x_start)


def get_text_xy_coords(stdscr, text, y_offset=0):
    _, x_mid = get_midpoint(stdscr)

    y_start = get_timer_xy_coords(stdscr)[0] + TIMER_HEIGHT + 1 + y_offset
    x_start = x_mid - len(text) // 2

    return (y_start, x_start)


def draw_help(stdscr):
    height, _ = stdscr.getmaxyx()
    stdscr.addstr(
        height - 3,
        1,
        "space - pause/resume    enter - skip    1 - pomodoro    2 - short break    3 - long break    CTRL+C - exit",
    )


def draw_pause_text(stdscr):
    # Delete help text
    height, _ = stdscr.getmaxyx()
    for y in range(1, 4):
        stdscr.move(height - y, 0)
        stdscr.clrtoeol()

    y, x = get_text_xy_coords(stdscr, TIMER_TEXT["pause"], -TIMER_HEIGHT - 1 - 2)
    stdscr.addstr(y, x, TIMER_TEXT["pause"])
    stdscr.move(0, 0)  # Move cursor away in case it's showing


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.keypad(True)

    timer_control_queue = Queue()

    def timer():
        num_pomodoro = 0
        timer_state = "pomodoro"
        goto_flag = False

        while True:
            text = TIMER_TEXT[timer_state]
            num_pomodoro_text = "#" + str(num_pomodoro)
            current_duration = TIMER_DURATION[timer_state]
            start_flag = True

            while current_duration >= 0:
                time_str = time.strftime(TIME_FORMAT, time.gmtime(current_duration))

                stdscr.clear()
                draw_timer(stdscr, *get_timer_xy_coords(stdscr), time_str)
                stdscr.addstr(
                    *get_text_xy_coords(stdscr, num_pomodoro_text), num_pomodoro_text
                )  # Print number of pomodoros finished just below the timer
                stdscr.addstr(
                    *get_text_xy_coords(stdscr, text, 1), text
                )  # Print current pomodoro state
                draw_help(stdscr)
                stdscr.move(0, 0)  # Move cursor away in case it's showing
                stdscr.refresh()

                if start_flag == True:
                    draw_pause_text(stdscr)
                    stdscr.refresh()
                    while True:
                        second_key = timer_control_queue.get()
                        if second_key == ord(" "):
                            start_flag = False
                            current_duration += 1
                            break
                else:
                    try:
                        key = timer_control_queue.get(
                            timeout=1
                        )  # This is where the 1 second "sleep" comes from
                        if key == ord(" "):
                            draw_pause_text(stdscr)
                            stdscr.refresh()
                            while True:
                                second_key = timer_control_queue.get()
                                if second_key == ord(" "):
                                    current_duration += 1
                                    break
                        elif key == ord("\n"):
                            break
                        elif key == ord("1"):
                            timer_state = "pomodoro"
                            goto_flag = True
                            break
                        elif key == ord("2"):
                            timer_state = "short_break"
                            goto_flag = True
                            break
                        elif key == ord("3"):
                            timer_state = "long_break"
                            goto_flag = True
                            break
                    except Empty:
                        pass

                current_duration -= 1

            if goto_flag == True:  # Skip changing pomodoro state
                goto_flag = False
                continue

            if timer_state == "pomodoro":
                if num_pomodoro != 0 and num_pomodoro % args.long_break_interval == 0:
                    timer_state = "long_break"
                else:
                    timer_state = "short_break"
                num_pomodoro += 1
            else:
                timer_state = "pomodoro"

            # beep()

    def timer_control():
        while True:
            key = stdscr.getch()
            timer_control_queue.put(key)

    timer_thread = threading.Thread(target=timer, daemon=True)
    timer_control_thread = threading.Thread(target=timer_control, daemon=True)
    timer_thread.start()
    timer_control_thread.start()
    timer_thread.join()
    timer_control_thread.join()

def console_script():
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    console_script()
