import argparse
import datetime
import os
import sys
import threading
import time
from functools import partial

import pyautogui
import screeninfo
from PIL import ImageGrab

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

valid_units = ["seconds", "minutes", "hours", "s", "m", "h"]
screens = screeninfo.get_monitors()

looping = True
screenshot_count = 0
screenshot_bytes = 0
    
def screenshot_loop(screen_bounds, outdir, delay, event):
    global screenshot_count, screenshot_bytes
    while looping:
        image = pyautogui.screenshot(region=screen_bounds)
        timestamp = datetime.datetime.now()
        path = os.path.join(outdir, timestamp.strftime("%Y-%m-%d_%H.%M.%S") + ".png")
        image.save(path)
        screenshot_bytes += os.stat(path).st_size
        screenshot_count += 1
        event.wait(timeout=delay)

def human_size(bytes, units=['B','KB','MB','GB','TB', 'PB', 'EB']):
    """
    Returns a human readable string representation of bytes.
    
    Source: https://stackoverflow.com/a/43750422
    """
    return str(bytes) + " " + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])

def parse_args():
    parser = argparse.ArgumentParser(description="Take <rate> screenshots per <unit> of the specified screen")
    parser.add_argument("rate", type=int, help="the rate at which to take screenshots")
    parser.add_argument("unit", metavar="unit", type=str.lower, help="the unit of the rate argument; must be one of " + str(valid_units),
                        choices=valid_units)
    parser.add_argument("--screen", dest="screen", metavar="<id>", const=None, type=int, nargs=1, default=0, action="store",
                        help="the screen of which to take screenshots")
    parser.add_argument("--outdir", dest="outdir", metavar="<path>", const=None, type=str, nargs=1, default=".", action="store",
                        help="the directory in which to save screenshots; by default, this is the current directory")
    parser.add_argument("--list-screens", dest="screens", action="store_true",
                        help="list available screens and exit")
    parser.add_argument("--silent", dest="silent", action="store_true",
                        help="do not print any output during normal operation")

    args = parser.parse_args()

    if(args.screens):
        if(len(screens) == 0):
            print("no screens available")
        else:
            for i, s in enumerate(screens):
                print(f"screen {i}: {s.width}x{s.height} at ({s.x}, {s.y}){' [primary]' if s.is_primary else ''}")
        exit()

    if len(screens) == 0:
        print("error: no screens available", file=sys.stderr)
        exit()

    screen_id = args.screen[0] if isinstance(args.screen, list) else args.screen

    if screen_id < 0 or screen_id >= len(screens):
        print("error: screen must be one of", [i for i in range(len(screens))], file=sys.stderr)
        exit()

    rate = args.rate[0] if isinstance(args.rate, list) else args.rate

    if args.unit == "s" or args.unit == "seconds":
        delay = 1 / rate
    elif args.unit == "m" or args.unit == "minutes":
        delay = 60 / rate
    elif args.unit == "h" or args.unit == "hours":
        delay = 3600 / rate

    screen = screens[screen_id]
    outdir = args.outdir[0] if isinstance(args.outdir, list) else args.outdir

    return (
        delay,
        (screen.x - min(min([screen.x for screen in screens]), 0), screen.y, screen.width, screen.height),
        os.getcwd() if outdir == "." else os.path.join(os.getcwd(), outdir),
        args.silent
    )

def main():
    global looping

    delay, screen_bounds, outdir, silent = parse_args()

    if os.path.exists(outdir):
        if not os.path.isdir(outdir):
            print("error: outdir path is a file", file=sys.stderr)
            exit()
    else:
        os.mkdir(outdir)

    e = threading.Event()
    start_time = time.time()
    thread = threading.Thread(target=screenshot_loop, args=(screen_bounds, outdir, delay, e))
    thread.start()

    spinner = ["|", "/", "-", "\\"]
    spinner_index = 0

    try:
        line_length = 0
        while True:
            if not silent:
                line = "<{0}> [{1}] {2} screenshot{3} ({4})".format(
                    spinner[spinner_index % len(spinner)],
                    datetime.timedelta(seconds=int(time.time() - start_time)),
                    screenshot_count,
                    " " if screenshot_count == 1 else "s",
                    human_size(screenshot_bytes)
                )
                if len(line) < line_length:
                    line += " " * (line_length - len(line))
                print(line, end="\r", flush=True)
                line_length = len(line)
                spinner_index += 1
            time.sleep(0.2)
    except KeyboardInterrupt:
        looping = False
        e.set()
        if not silent:
            print("Process terminated by user after", str(datetime.timedelta(seconds=int(time.time() - start_time))))
        exit()

if __name__ == "__main__":
    main()
