from turtle import title
from colorama import Fore, Back, Style, Cursor
from datetime import datetime
from colorama import init
init()


def get_ANSI_code(name: str) -> str:
    ansi_code_list = {
        'reset_all': Style.RESET_ALL,
        'reset': Fore.RESET,
        'bright': Style.BRIGHT,
        'dim': Style.DIM,
        'normal': Style.NORMAL,
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'grey': Style.BRIGHT + Fore.BLACK,
        'back_black': Back.BLACK,
        'back_red': Back.RED,
        'back_green': Back.GREEN,
        'back_yellow': Back.YELLOW,
        'back_blue': Back.BLUE,
        'back_magenta': Back.MAGENTA,
        'back_cyan': Back.CYAN,
        'back_white': Back.WHITE,
        'back_grey': Style.BRIGHT + Back.BLACK,
    }

    for ansi, value in ansi_code_list.items():
        if ansi == name:
            return value
    raise Exception(f'ANSI code not found')


def style(text: str, styles: str) -> str:
    if styles:
        styles = styles.split()
        for style in styles:
            text = get_ANSI_code(style) + str(text)
        return str(text + get_ANSI_code('reset_all'))
    return text


def get_time() -> str:
    time = datetime.now()
    hour = str(time.hour)
    minute = str(time.minute)
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute


def timed_print(*text, styles: str = "back_white black dim", end="\n") -> str:
    date = datetime.now()
    print(style(date.time(), styles), *text, end=end)
    return text


def log(title: str) -> str:
    date = datetime.now()
    print(style(" " + str(date.time()) + " ", "back_cyan white dim"), title)
    return title


def warn(title: str) -> str:
    date = datetime.now()
    print(style(" " + str(date.time()) +
          " ", "back_yellow white dim"), style("Warning", "yellow dim"), title)
    return title


def success(title: str) -> str:
    date = datetime.now()
    print(style(" " + str(date.time()) + " ",
          "back_green bright white dim"), title)
    return title


def concatinate(*text, separator: str = " "):
    return separator.join(text)


if __name__ == "__main__":
    timed_print("test", "test", styles="black dim")
