"""
ANSI/VT escape codes for most common terminal operations.

VT100 is a standard for terminal emulation escape codes. It is specifies cursor movement.
A lot of people say VT100, but they mean ANSI escape codes.

VT220 introduced a lot of new features, such as color.
Then, xterm came along and added even more features, such as mouse support.

These are all grouped under the name "ANSI escape codes", which is a bit
misleading, as ANSI is a standards body, and these are not all standards.

See also:
- https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
- https://bluesock.org/~willg/dev/ansi.html#ansicodes

For fun:
- https://xn--rpa.cc/irl/term.html
- https://github.com/jart/cosmopolitan/blob/master/tool/build/lib/pty.c
"""

ESC = "\x1b"
CSI = f"{ESC}["  # "Control Sequence Introducer"

# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#set-mode
screen_set_alternate = f"{CSI}?1049h"
screen_set_normal = f"{CSI}?1049l"
screen_save = f"{CSI}?47h"
screen_restore = f"{CSI}?47l"
screen_enable_line_wrap = f"{CSI}?7h"
screen_disable_line_wrap = f"{CSI}?7l"
screen_enable_256_colors = f"{CSI}?19h"
screen_disable_256_colors = f"{CSI}?19l"


cursor_set_visible = f"{CSI}?25h"
cursor_set_invisible = f"{CSI}?25l"

# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#cursor-controls
def cursor_move_to(line, column):
    """
    Move the cursor to the specified line and column
    """
    return f"{CSI}{line};{column}H"


def cursor_move_up(count):
    """
    Move the cursor up `count` lines
    """
    return f"{CSI}{count}A"


def cursor_move_down(count):
    """
    Move the cursor down `count` lines
    """
    return f"{CSI}{count}B"


def cursor_move_forward(count):
    """
    Move the cursor forward `count` columns
    """
    return f"{CSI}{count}C"


def cursor_move_backward(count):
    """
    Move the cursor backward `count` columns
    """
    return f"{CSI}{count}D"


cursor_save_position = f"{CSI}s"
cursor_restore_position = f"{CSI}u"
cursor_blinking_block = f"{CSI}?12h"
cursor_steady_block = f"{CSI}?12l"
cursor_blinking_underline = f"{CSI}?25h"
cursor_steady_underline = f"{CSI}?25l"
cursor_blinking_bar = f"{CSI}?17h"
cursor_steady_bar = f"{CSI}?17l"


# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#erase-functions
erase_display = f"{CSI}2J"
erase_to_end_of_display = f"{CSI}0J"
erase_to_start_of_display = f"{CSI}1J"
erase_line = f"{CSI}2K"
erase_to_end_of_line = f"{CSI}0K"
erase_to_start_of_line = f"{CSI}1K"

# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#colors--graphics-mode
style_reset = f"{CSI}0m"
style_reset = f"{CSI}0m"
style_bold = f"{CSI}1m"
style_dim = f"{CSI}2m"
style_italic = f"{CSI}3m"
style_underline = f"{CSI}4m"
style_blink = f"{CSI}5m"
style_reverse = f"{CSI}7m"
style_hidden = f"{CSI}8m"
style_strikethrough = f"{CSI}9m"

# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes
color_black = f"{CSI}30m"
color_red = f"{CSI}31m"
color_green = f"{CSI}32m"
color_yellow = f"{CSI}33m"
color_blue = f"{CSI}34m"
color_magenta = f"{CSI}35m"
color_cyan = f"{CSI}36m"
color_white = f"{CSI}37m"

color_bright_black = f"{CSI}90m"
color_bright_red = f"{CSI}91m"
color_bright_green = f"{CSI}92m"
color_bright_yellow = f"{CSI}93m"
color_bright_blue = f"{CSI}94m"
color_bright_magenta = f"{CSI}95m"
color_bright_cyan = f"{CSI}96m"
color_bright_white = f"{CSI}97m"

color_bg_black = f"{CSI}40m"
color_bg_red = f"{CSI}41m"
color_bg_green = f"{CSI}42m"
color_bg_yellow = f"{CSI}43m"
color_bg_blue = f"{CSI}44m"
color_bg_magenta = f"{CSI}45m"
color_bg_cyan = f"{CSI}46m"
color_bg_white = f"{CSI}47m"

color_bg_bright_black = f"{CSI}100m"
color_bg_bright_red = f"{CSI}101m"
color_bg_bright_green = f"{CSI}102m"
color_bg_bright_yellow = f"{CSI}103m"
color_bg_bright_blue = f"{CSI}104m"
color_bg_bright_magenta = f"{CSI}105m"
color_bg_bright_cyan = f"{CSI}106m"
color_bg_bright_white = f"{CSI}107m"


def color_256(fg_color: int = None, bg_color: int = None):
    """
    Set the foreground and background colors to the specified 256-color values.
    Resets style if both are None.
    """
    if fg_color is None and bg_color is None:
        return style_reset
    if fg_color is None:
        return f"{CSI}48;5;{bg_color}m"
    if bg_color is None:
        return f"{CSI}38;5;{fg_color}m"
    return f"{CSI}38;5;{fg_color};48;5;{bg_color}m"
