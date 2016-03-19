COLOUR_END = "\033[0m"
MAIN_COLOURS = {
    "cyan": "\033[46m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "light_red": "\033[101m",
    "light_green": "\033[102m",
    "light_blue": "\033[104m",
    "light_magenta": "\033[105m",
    "light_cyan": "\033[106m",
}
AUX_COLOURS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "light_red": "\033[91m",
    "light_green": "\033[92m",
    "light_yellow": "\033[93m",
    "light_blue": "\033[94m",
    "light_magenta": "\033[95m",
    "light_cyan": "\033[96m",
}
MAIN_COLOURS_SET = {MAIN_COLOURS[key] for key in MAIN_COLOURS}
AUX_COLOURS_SET = {AUX_COLOURS[key] for key in AUX_COLOURS}
FULL_COLOURS_SET = MAIN_COLOURS_SET.union(AUX_COLOURS_SET)
