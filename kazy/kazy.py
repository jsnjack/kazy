#!/usr/bin/env python3
import random
import re
import sys

from colours import COLOUR_END, MAIN_COLOURS_SET, FULL_COLOURS_SET, AUX_COLOURS_SET, BACKUP_COLOURS_SET


def main():
    selectors = parse_args()

    regexp = re.compile("|".join("(" + item["selector"] + ")" for item in selectors))
    while True:
        try:
            line = sys.stdin.readline()
        except StopIteration:
            break
        else:
            splitted = regexp.split(line[:-1])
            for item in selectors:
                splitted = colourify(item, splitted)
            colourful_text = "".join(item for item in splitted if item)

            print(colourful_text)


def colourify(item, splitted):
    """
    Add colours to the matched string
    """
    for idx, el in enumerate(splitted):
        if el == item["selector"]:
            splitted[idx] = item["colour"] + splitted[idx] + COLOUR_END
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
    available = MAIN_COLOURS_SET.difference(in_use)
    if available:
        colour = available.pop()
    else:
        available = AUX_COLOURS_SET.difference(in_use)
        if available:
            colour = available.pop()
        else:
            available = BACKUP_COLOURS_SET.difference(in_use)
            if available:
                colour = available.pop()
            else:
                colour = random.choice(list(FULL_COLOURS_SET))
    return colour

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
