#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2023 Andrew Spangler
Licensed under GPLv3
This file is part of py_simple_morse_code.py
"""


import pyaudio
import numpy as np
import scipy
import scipy.signal

from .CONSTANTS import (
    DEFAULT_MIN_TONE,
    DEFAULT_MAX_TONE,
    DEFAULT_SAMPLE_SIZE,
    DEFAULT_SAMPLE_RATE,
    DEFAULT_HIGH_PASS_FREQUENCY,
    DEFAULT_LOW_PASS_FREQUENCY,
)


class SignalProcessor:
    """Non-blocking CW signal processor. The .process() method returns true if a CW tone was found in the signal."""

    def __init__(
        self,
        mic_index: int = 0,
        min_tone: int = DEFAULT_MIN_TONE,
        max_tone: int = DEFAULT_MAX_TONE,
        sample_size: int = DEFAULT_SAMPLE_SIZE,
        sample_rate: int = DEFAULT_SAMPLE_RATE,
        high_pass_frequency: int = DEFAULT_HIGH_PASS_FREQUENCY,
        low_pass_frequency: int = DEFAULT_LOW_PASS_FREQUENCY,
    ):
        self.mic_index = mic_index
        self.sample_size = sample_size
        self.sample_rate = sample_rate
        self.min_tone = min_tone
        self.max_tone = max_tone
        # Calculate nyquist once
        self.nyquist = sample_rate / 2
        # Bandpass filter values to reduce noise
        self.high_pass_frequency = high_pass_frequency
        self.low_pass_frequency = low_pass_frequency
        # Set up audio session
        self.audio_session = pyaudio.PyAudio()
        self.stream = None

    def start_session(self) -> None:
        """Start the audio stream. *Returns None*"""
        if not self.stream is None:
            raise ValueError("Active signal processor session exists")
        # Open pyaudio stream
        self.stream = self.audio_session.open(
            format=pyaudio.paFloat32,
            channels=1,
            input_device_index=self.mic_index,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.sample_size,
        )

    def end_session(self) -> None:
        """Ends the audio stream. *Returns None*"""
        if self.stream is None:
            raise ValueError("No active signal processor session exists to stop")
        self.stream.stop_stream()
        self.stream.close()

    def process(self) -> bool:
        """Process a chunk of the audio stream from the buffer. *Returns None*"""
        if self.stream is None:
            raise ValueError("No active signal processor session exists")
        # This only blocks if there is an insufficient buffer
        buf = self.stream.read(self.sample_size)
        samples = np.frombuffer(buf, dtype=np.float32)
        # Apply fft
        fft_array = np.fft.fft(samples)
        # Calculate butterworth coefficients for bandpass
        denominator, numerator = scipy.signal.butter(
            5,  # Use butterworth order number of 5
            [
                self.high_pass_frequency / self.nyquist,
                self.low_pass_frequency / self.nyquist,
            ],
            btype="band",
        )
        # Apply bandpass filter to reduce signal noise
        fft_array = scipy.signal.lfilter(denominator, numerator, fft_array)
        # Get frequency bins
        freq_array = np.fft.fftfreq(samples.size)
        # Get the index of the peak frequency
        peak_index = np.argmax(np.abs(fft_array) ** 2)
        # Get peak frequency
        freq = np.abs(freq_array[peak_index]) * self.sample_rate
        # Return bool indicating peak frequency is or isn't in specified range
        return bool(int(freq) > self.min_tone and int(freq) < self.max_tone)
