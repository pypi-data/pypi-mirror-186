#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2023 Andrew Spangler
Licensed under GPLv3
This file is part of py_simple_morse_code.py
"""


import time
import pyaudio
import numpy as np

# Set up audio
_MORSE_AUDIO_HOOK = pyaudio.PyAudio()

from .CONSTANTS import (
    DEFAULT_TONE,
    DEFAULT_NUM_DEADBEATS,
    DEFAULT_WORDS_PER_MINUTE,
    DEFAULT_STATE_DEBOUNCE,
    DEFAULT_SAMPLE_RATE,
    DURATIONS,
    UNKNOWN_CHAR,
    CHAR_TO_MORSE_MAP,
    MORSE_TO_CHAR_MAP,
)


def encode_string_to_morse(
    in_str: str,  # Your input string
    short_char: str = ".",  # Change to overwrite short pulse char
    long_char: str = "-",  # Change to overwrite long pulse char
    sep_char: str = " ",  # Change to overwrite separator char
    replace_on_unknown: bool | str = UNKNOWN_CHAR,  # Unknown char, None to raise error
    verbose: bool = True,
) -> str:
    """Encodes text to morse code dots and dashes. *Returns a string*"""
    if verbose:
        print(f"Encoding string {in_str} to morse...")

    # Sanitize input string, runs until fully sanitized
    prev_string = None  # Used to check if string changed since last pass
    while not prev_string == in_str:
        prev_string = in_str
        in_str = in_str.strip().replace("\n", "").replace("  ", " ")

    morse = ""
    for c in in_str:
        if c == " ":
            # add another sep_char to make word separator
            morse += sep_char
            continue

        if not (char := CHAR_TO_MORSE_MAP.get(c)):
            if not replace_on_unknown:
                raise LookupError(
                    f"Could not find morse pattern for char {c} in lookup table"
                )
            char = CHAR_TO_MORSE_MAP.get(replace_on_unknown)
        morse += char + sep_char

    morse = morse.strip(sep_char).replace(".", short_char).replace("-", long_char)

    if verbose:
        print(f"Encoded string: {morse}\n")

    return morse


def decode_morse_to_string(
    morse: str,
    char_sep: str = " ",
    word_sep: str = "  ",
    replace_on_unknown: str | bool = UNKNOWN_CHAR,
) -> str:
    """Decodes morse dots and dashes to plaintext. *Returns a string*"""
    # Handle standard slash wordsep
    morse = morse.strip(" ").replace(" / ", "  ")

    out_str = ""

    for word in morse.split(word_sep):
        for char_pattern in word.split(char_sep):
            if not (decoded_char := MORSE_TO_CHAR_MAP.get(char_pattern)):
                if not replace_on_unknown:
                    raise LookupError(
                        f"Could not find char for morse pattern {char_pattern} in lookup table"
                    )
                # decoded_char = CHAR_TO_MORSE_MAP.get(replace_on_unknown)
                decoded_char = replace_on_unknown
            out_str += decoded_char
        out_str += " "

    return out_str.lstrip(UNKNOWN_CHAR).lstrip("\n")


def encode_morse_to_beats(morse: str, verbose: bool = True) -> list:
    """Converts dots and dashes to a beats list. *Returns a list of bools*"""
    if not len(morse):
        return ""
    if verbose:
        print(f"Encoding morse {morse} to beats")
    beats, first = [], True
    for word in morse.split("  "):
        if not first:  # Skip wordsep on first
            # Expand charsep to wordsep
            beats.extend([False for i in range(4)])
        first = False
        for char_pattern in word.split(" "):
            for symbol in char_pattern:
                beats.extend(True for i in range(DURATIONS[symbol]))
                beats.append(False)  # Beat between chars
            # Expand beatsep to charsep
            beats.extend([False for i in range(2)])
    if verbose:
        print(f"Encoded morse: {beats}\n")
    return beats


def encode_string_to_beats(in_str: str, verbose: bool = True) -> list:
    """Converts a plaintext string to a beats list. *Returns a list of bools*"""
    morse = encode_string_to_morse(in_str, verbose=verbose)
    return encode_morse_to_beats(morse, verbose=verbose)


def make_morse_visual_from_beats(beats: list) -> str:
    """Converts a beats list to a visual representation in string form \
    using block chars (unicode char 2588). *Returns a string*"""
    visual = ""
    # chars = ["_", "-"]
    chars = [" ", "\u2588"]
    for b in beats:
        visual += chars[b]
    return visual


def encode_beats_to_waveform(
    beats: list,
    tone: int = DEFAULT_TONE,
    words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    verbose: bool = True,
    volume: float = 0.75,  # Prevent clipping
    deadbeats: int = DEFAULT_NUM_DEADBEATS,  # silent beets at the end of the waveform
) -> np.ndarray:
    """Encode a beats list into a waveform. *Returns a float32 1-dimensional numpy array*"""

    if verbose:
        print(f"Encoding beats to waveform: {beats}")

    start = time.time()

    beat_duration = calculate_beat_duration_from_wpm(words_per_minute)

    # Generate 3 beat sample at given tone
    tone_sample = (
        np.sin(
            2 * np.pi * np.arange(sample_rate * beat_duration * 3) * tone / sample_rate
        )
    ).astype(np.float32)

    silent_sample = np.zeros((len(tone_sample) // 3), dtype=np.float32)

    samples = {
        1: tone_sample[: len(tone_sample) // 3],
        3: tone_sample,
    }

    waveform = []
    # Walk through beats and assemble waveform from samples
    beatcount = len(beats)
    index, count, state = 0, None, None
    while index < beatcount:
        if state is None:
            state = beats[index]
            count = 1
            index += 1
        # Counts the number of beats between state changes
        while index < beatcount and beats[index] == state:
            count += 1
            index += 1

        if state:
            waveform.extend(samples[count])
        else:
            for i in range(count):
                waveform.extend(silent_sample)

        count = 0
        state = None

    # Add deadbeats to end
    for i in range(deadbeats):
        waveform.extend(silent_sample)

    waveform = np.asarray(waveform, dtype=np.float32)

    end = time.time()
    if verbose:
        print(f"Encoding took {end-start}")
        print(f"Waveform is {len(waveform)} samples\n")

    return waveform


def play_waveform(
    waveform: bytes, format=pyaudio.paFloat32, sample_rate=DEFAULT_SAMPLE_RATE
) -> None:
    """Plays a waveform. *Return None*"""
    stream = _MORSE_AUDIO_HOOK.open(
        format=format, channels=1, rate=sample_rate, output=True
    )
    stream.write(waveform.tobytes())
    stream.stop_stream()
    stream.close()


def play_string(
    in_str: str,
    tone: int = DEFAULT_TONE,
    words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    verbose: bool = True,
) -> None:
    """Converts plaintext to a waveform and play it on system speakers. *Returns None*"""
    beats = encode_string_to_beats(in_str, verbose)
    waveform = encode_beats_to_waveform(
        beats, tone, words_per_minute, sample_rate, verbose
    )
    play_waveform(waveform, sample_rate=DEFAULT_SAMPLE_RATE)


def play_morse(
    morse: str,
    tone: int = DEFAULT_TONE,
    words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    verbose: bool = True,
) -> None:
    """Converts dots and dashes to a waveform and plays it on system speakers. *Returns None*"""
    beats = encode_morse_to_beats(morse, verbose)
    waveform = encode_beats_to_waveform(
        beats, tone, words_per_minute, sample_rate, verbose
    )
    play_waveform(waveform, rate=sample_rate)


def encode_string_to_waveform(
    in_str: str,
    tone: int = DEFAULT_TONE,
    words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    verbose: bool = True,
) -> np.ndarray:
    """Encode a plaintext string to a waveform. *Returns a float32 1-dimensional numpy array*"""
    beats = encode_string_to_beats(in_str)
    return encode_beats_to_waveform(beats, tone, words_per_minute, sample_rate, verbose)


def encode_morse_to_waveform(
    morse: str,
    tone: int = DEFAULT_TONE,
    words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    verbose: bool = True,
) -> np.ndarray:
    """Encode a morse string to a waveform. *Returns a float32 1-dimensional numpy array*"""
    beats = encode_morse_to_beats(morse)
    return encode_beats_to_waveform(beats, tone, words_per_minute, sample_rate, verbose)


def calculate_beat_duration_from_wpm(words_per_minute: int) -> float:
    """Caclulate beat duration from words per minute. *Returns a float*"""
    return (1200.0 / words_per_minute) / 1000.0


class MorseCodeTranslator:
    """A low-level morse code translator. Inputs should be debounced / sanitized \
    before being passed to the .update(state:bool) method. Tolerance only affects \
    word-sep deadbeats to account for hesitation / early resumes between words."""

    def __init__(
        self,
        words_per_minute: int = DEFAULT_WORDS_PER_MINUTE,
        debounce_time: float = DEFAULT_STATE_DEBOUNCE,
        tolerance: int = 0,  # 1: low tolerance, 2: high tolerance
    ):
        self.start = time.time()

        self.words_per_minute = words_per_minute
        self.debounce_time = debounce_time
        self.tolerance = tolerance

        self.last_state = None
        self.last_state_change = None
        self.unparsed_content = ""
        self.parsed_content = ""

    def update(self, state: bool) -> None:
        """
        Call this whenever input state changes.
        Alternatively call this at a set frequency with the current state.
        *Returns None*
        """
        if state == self.last_state:
            return
        timestamp = time.time()
        last_state = self.last_state
        last_state_change = self.last_state_change
        self.last_state = state
        self.last_state_change = timestamp
        if not last_state_change:  # skip on first pulse
            return

        dt = timestamp - last_state_change
        if dt < self.debounce_time:
            # Ignore too fast state changes
            self.last_state_change = last_state_change
            return
        beat_count = round(dt / calculate_beat_duration_from_wpm(self.words_per_minute))
        # Handle large beat errors at wide tolerance
        if self.tolerance > 1 and beat_count in (5, 6, 8, 9):
            beat_count = 7
        elif self.tolerance > 0 and beat_count in (6, 8):
            beat_count = 7

        if beat_count:
            if not state:  # Going off high state
                if beat_count == 1:
                    self.unparsed_content += "."
                elif beat_count == 3:
                    self.unparsed_content += "-"
                else:
                    print(f"UNKNOWN BEAT COUNT - HIGH:{beat_count}")
                    self.unparsed_content += "?"
            else:  # Going into high state
                if beat_count == 1:
                    self.unparsed_content += ""
                elif beat_count == 3:
                    self.unparsed_content += " "
                elif beat_count == 7:
                    self.unparsed_content += "  "
                elif beat_count > 7:
                    # Add newline when pause is greater than wordsep
                    # Keep in mind that this may take up to 10 beats to trigger
                    # at higher tolerance values
                    self.unparsed_content += "\n"
                else:
                    print(f"UNKNOWN BEAT COUNT - LOW:{beat_count}")
        self.unparsed_content = self.unparsed_content.lstrip()
        self.parsed_content = decode_morse_to_string(self.unparsed_content)
