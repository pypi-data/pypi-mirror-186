#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2023 Andrew Spangler
Licensed under GPLv3
This file is part of py_simple_morse_code.py
"""


# Tone for generated audio
DEFAULT_TONE = 1000  # Hz
# Min CW tone for live processing
DEFAULT_MIN_TONE = 600  # Hz
# Max CW tone for live processing
DEFAULT_MAX_TONE = 1500  # Hz
# Sample size for live processing
DEFAULT_SAMPLE_SIZE = 512
# Sample rate in samples / second
DEFAULT_SAMPLE_RATE = 32000
# High pass cutoff in Hz
DEFAULT_HIGH_PASS_FREQUENCY = 4
# Low pass cutoff in Hz
DEFAULT_LOW_PASS_FREQUENCY = 10000
# Default number of deadbeats to add to end of generated audio
DEFAULT_NUM_DEADBEATS = 0
# # Default duration of a beat in seconds
# DEFAULT_BEAT_DURATION = 0.1
# Default words per minute rate for transmit and receive
DEFAULT_WORDS_PER_MINUTE = 24
# Min time between allowed state changes
DEFAULT_STATE_DEBOUNCE = 0.01
# Durations for short and long pulses
DURATIONS = {
    ".": 1,  # Short pulse, one unit
    "-": 3,  # Long pulse, three units
}

UNKNOWN_CHAR = "?"

MORSE_CODE_LETTERS_MAP = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}
# Add uppercase
for char in list(MORSE_CODE_LETTERS_MAP.keys()):
    MORSE_CODE_LETTERS_MAP[char.upper()] = MORSE_CODE_LETTERS_MAP[char]

MORSE_CODE_NUMBERS_MAP = {
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

# Not 100% standard but widely used
MORSE_CODE_PUNCTUATION_MAP = {
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "+": ".-.-.",
    "=": " -...-",
    "_": "..--.-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    "$": "...-..-",
    "@": ".--.-.",
    '"': ".-..-.",
    "\b": "........",  # Backspace
}

# Make master char encoder map
CHAR_TO_MORSE_MAP = MORSE_CODE_LETTERS_MAP.copy()
CHAR_TO_MORSE_MAP.update(MORSE_CODE_NUMBERS_MAP)
CHAR_TO_MORSE_MAP.update(MORSE_CODE_PUNCTUATION_MAP)

# Invert char to morse lookup.
MORSE_TO_CHAR_MAP = {v: k for k, v in CHAR_TO_MORSE_MAP.items()}
# Add unknown char and newline handlers
MORSE_TO_CHAR_MAP.update({UNKNOWN_CHAR: UNKNOWN_CHAR, "\n": "\n"})
