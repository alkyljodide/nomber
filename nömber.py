# adapted from Harri: github.com/StenoHarri/steno-Python-dictionaries/blob/main/Harri_numbers.py 
# written by Grahp: github.com/Grahp/dotfiles/blob/main/plover/.config/plover/alky-numbers.py

import re
import os

LONGEST_KEY = 1

NUMBER_KEY = "#"

STARTERS = {
    "#TPH": "{&}",
    "#TPH*": " ",
    "#P": "0.",
    "#P*": "{^}.",
    "#TK": "$",
    "#STK": "S$",
    "#TKEU": "€",
    "#TKPW": "₿",
    "#TKP": "£",
    "#TKRU": "CN¥",
    "#TKRE": "JP¥",
}

BINDERS = {
   "#KWR": {"prefix": " ",
            "suffix": "hrs"},
   "#KWR*": {"prefix": "{^:}",
            "suffix": " {meridiem}"}
}

VOWELS_NUMBERS = {
    "A": "45",
    "AO": "30",
    "O": "15",
    "E": "00"
}

NUMPAD_1 = {
    "F": "1",
    "FP": "2",
    "P": "3",
    "FR": "4",
    "FRPB": "5",
    "PB": "6",
    "R": "7",
    "RB": "8",
    "B": "9"
}

NUMPAD_2 = {
    "L": "1",
    "LT": "2",
    "T": "3",
    "LG": "4",
    "LGTS": "5",
    "TS": "6",
    "G": "7",
    "GS": "8",
    "S": "9"
}

def convert_numbers_to_strokes(stroke: str) -> str:
    if any(char.isdigit() for char in stroke):
        stroke_list = list(stroke)
        number_to_stroke = ["O", "S", "T", "P", "H", "A", "F", "P", "L", "T"]
        for i, char in enumerate(stroke_list):
            if char.isdigit():
                stroke_list[i] = number_to_stroke[int(char)]
        stroke = "#" + "".join(stroke_list)
    return stroke

def lookup(chord: tuple[str]) -> str:
    stroke = chord[0]

    if NUMBER_KEY not in STROKE:
        raise KeyError

    MATCH = re.fullmatch(r'(\#?S?T?K?P?W?H?R?)(A?O?E?U?)([-*]?)([FRPB]*)([LGTS]*)', STROKE)
    if MATCH is None:
        raise KeyError

    (LEFT_HAND, VOWELS, SEPARATOR, GROUP_NUMPAD_1, GROUP_NUMPAD_2) = MATCH.groups()

    output = ""

    # Prefixes
    for STARTER in STARTERS:
        if STARTER in LEFT_HAND:
            output += STARTERS[STARTER]

    # Binders
    for BINDER in BINDERS
        if BINDER in LEFT_HAND:
            output += 

    # Numpad
    if GROUP_NUMPAD_1 in NUMPAD_1:
        output += NUMPAD_1[GROUP_NUMPAD_1]
        if GROUP_NUMPAD_2 is '':
            output += '0'
    if GROUP_NUMPAD_2 is not '':
        output += NUMPAD_2[GROUP_NUMPAD_2]

    if VOWELS in VOWELS_NUMBERS:
        output += VOWELS_NUMBERS[VOWELS]

    return output

    # Clock
    if "#KWR*" in STROKE:
      hour_output = stroke_1
      minute_output = stroke_2

      hour_int = int(hour_output)
      minute_int = int(minute_output)
      meridiem = ['a.m', 'p.m']
        if hour_int > 12: 
        hour_int -= 12
        meridiem = 'pm'
        elif hour_int == 12:
        meridiem = 'pm'
        elif hour_int == 0:
        meridiem = 'am'
      else:
        meridiem = 'am'
     return "{hour_int}:{minute_int} {meridiem}"
