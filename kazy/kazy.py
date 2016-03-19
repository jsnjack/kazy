#!/usr/bin/env python3
import random
import re
import sys

COLOUR_END = "\033[0m"
COLOURS = {
    "cyan": "\033[46m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magents": "\033[45m",
}
COLOURS_SET = {COLOURS[key] for key in COLOURS}


def main():
    # Read piped data
    text = sys.stdin.read()

    selectors = parse_args()

    regexp = "|".join("(" + item["selector"] + ")" for item in selectors)
    splitted = re.split(regexp, text)
    for item in selectors:
        splitted = colourify(item, splitted)
    colourful_text = "".join(item for item in splitted if item)

    print(colourful_text)


def colourify(item, splitted):
    """
    Add colours to the matched string
    """
    while item["selector"] in splitted:
        index = splitted.index(item["selector"])
        splitted[index] = item["colour"] + splitted[index] + COLOUR_END
    return splitted


def parse_args():
    """
    Construct selectors object that contains selector and colour information
    """
    args = sys.argv[1:]
    selectors = []
    for item in args:
        selectors.append({
            "selector": item,
            "colour": get_colour(selectors)
        })
    return selectors


def get_colour(selectors):
    """
    Returns unique colour for every selector
    """
    in_use = {item["colour"] for item in selectors}
    available = COLOURS_SET.difference(in_use)
    if available:
        colour = available.pop()
    else:
        colour = random.choice(list(COLOURS_SET))
    return colour

if __name__ == "__main__":
    main()