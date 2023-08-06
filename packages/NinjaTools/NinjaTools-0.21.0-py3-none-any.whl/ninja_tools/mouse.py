import ctypes
import math
from random import randint
from time import sleep

MOUSEEVENTF_MOVE = 0x0001  # mouse move
MOUSEEVENTF_LEFTDOWN = 0x0002  # left button down
MOUSEEVENTF_LEFTUP = 0x0004  # left button up
MOUSEEVENTF_RIGHTDOWN = 0x0008  # right button down
MOUSEEVENTF_RIGHTUP = 0x0010  # right button up
MOUSEEVENTF_MIDDLEDOWN = 0x0020  # middle button down
MOUSEEVENTF_MIDDLEUP = 0x0040  # middle button up
MOUSEEVENTF_WHEEL = 0x0800  # wheel button rolled
MOUSEEVENTF_ABSOLUTE = 0x8000  # absolute move
SM_CXSCREEN = 0
SM_CYSCREEN = 1

ctypes.windll.user32.SetProcessDPIAware()
screen_width = ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN)
screen_height = ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN)
__event = ctypes.windll.user32.mouse_event


def click(right: bool = False, left: bool = False, middle: bool = False, double_click: bool = False, pause: int = 0):
    if double_click:
        down(right=right, left=left, middle=middle)
        delay(pause)
        up(right=right, left=left, middle=middle)

        delay(150)

        down(right=right, left=left, middle=middle)
        delay(pause)
        up(right=right, left=left, middle=middle)

    else:
        down(right=right, left=left, middle=middle)
        delay(pause)
        up(right=right, left=left, middle=middle)


def down(right: bool = False, left: bool = False, middle: bool = False):
    left = not any((right, left, middle))
    press = __get_button(right=right, left=left, middle=middle)
    __event(press[0], 0, 0, 0, 0)


def up(right: bool = False, left: bool = False, middle: bool = False):
    left = not any((right, left, middle))
    press = __get_button(right=right, left=left, middle=middle)
    __event(press[1], 0, 0, 0, 0)


def move(x: int, y: int):
    x, y = __normalize_xy(x, y)
    __event(MOUSEEVENTF_MOVE + MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


# Shift the mouse to x, y regardless of the current position
def shift(x: int, y: int):
    __event(MOUSEEVENTF_MOVE, x, y, 0, 0)


def __normalize_xy(x: int, y: int):
    old_position = get_position()
    x = x if x != -1 else old_position[0]
    y = y if y != -1 else old_position[1]
    x = math.floor(65536 * x / screen_width + 1)
    y = math.floor(65536 * y / screen_height + 1)

    return x, y


def __get_button(right: bool = False, left: bool = False, middle: bool = False):
    if sum((right, left, middle)) > 1:
        raise Error("Error: only 1 button option is allowed!")
    if right:
        return MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP
    if left:
        return MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
    if middle:
        return MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP


def is_pressed(code):
    return ctypes.windll.user32.GetKeyState(code) & 0x8000


def get_position():
    p = Point()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(p))

    return p.x, p.y


def delay(seconds: float = 0):
    if seconds == 0:
        sleep((randint(50, 60) * 0.001))
    else:
        sleep(seconds)


class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
