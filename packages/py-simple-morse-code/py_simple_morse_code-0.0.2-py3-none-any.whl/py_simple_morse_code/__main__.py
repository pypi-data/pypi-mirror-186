#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2023 Andrew Spangler
Licensed under GPLv3
This file is part of py_simple_morse_code.py
Some portions of the GUI code found in this file come from py_simple_ttk
"""

import time
import platform
import threading
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.filedialog import asksaveasfilename
from typing import Callable
from scipy.io import wavfile
from .py_simple_morse_code import (
    decode_morse_to_string,
    encode_morse_to_beats,
    encode_string_to_morse,
    encode_string_to_waveform,
    make_morse_visual_from_beats,
    MorseCodeTranslator,
    play_string,
)

from .signal_processing import SignalProcessor

from .CONSTANTS import (
    DEFAULT_SAMPLE_RATE,
    DEFAULT_WORDS_PER_MINUTE,
)

if __name__ == "__main__":

    def play(in_str: str, tone: int, words_per_minute: int) -> None:
        threading.Thread(
            target=lambda: play_string(
                in_str,
                tone=tone,
                words_per_minute=words_per_minute,
                verbose=False,
            )
        ).start()

    def export(filename: str, in_str: str, tone: int, words_per_minute: float) -> None:
        if filename:
            waveform = encode_string_to_waveform(
                in_str, tone=tone, words_per_minute=words_per_minute
            )
            wavfile.write(filename, DEFAULT_SAMPLE_RATE, waveform)

    # Widgets with scroll bars that appear when needed and supporting code
    class Scroller(object):
        """Use to wrap an object with scrollbars"""

        def __init__(self, parent: ttk.Frame):
            try:
                vsb = ttk.Scrollbar(parent, orient="vertical", command=self.yview)
            except:
                pass
            hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.xview)

            try:  # Fails if vsb instantiation failed
                self.configure(yscrollcommand=self._scroll(vsb))
            except:
                pass
            self.configure(xscrollcommand=self._scroll(hsb))

            self.grid(column=0, row=0, sticky="nsew")
            try:
                vsb.grid(column=1, row=0, sticky="ns")
            except:
                pass
            hsb.grid(column=0, row=1, sticky="ew")

            parent.grid_columnconfigure(0, weight=1)
            parent.grid_rowconfigure(0, weight=1)

            methods = (
                tk.Pack.__dict__.keys()
                | tk.Grid.__dict__.keys()
                | tk.Place.__dict__.keys()
            )

            for method in methods:
                if method[0] != "_" and method not in ("config", "configure"):
                    setattr(self, method, getattr(parent, method))

        @staticmethod
        def _scroll(bar) -> Callable:
            """Hide and show scrollbar as needed."""

            def hide(start, end) -> None:
                start, end = float(start), float(end)
                if start <= 0.0 and end >= 1.0:
                    bar.grid_remove()
                else:
                    bar.grid()
                bar.set(start, end)

            return hide

        def __str__(self) -> str:
            return str(self.parent)

    def _create_container(func: Callable) -> Callable:
        """Creates a tk Frame with a given parent, and uses this new frame to place the scrollbars and the widget."""

        def wrapped(cls, parent, **kw) -> object:
            container = ttk.Frame(parent)
            container.bind("<Enter>", lambda e: _bound_to_mousewheel(e, container))
            container.bind("<Leave>", lambda e: _unbound_to_mousewheel(e, container))
            return func(cls, container, **kw)

        return wrapped

    def _bound_to_mousewheel(event, widget) -> None:
        child = widget.winfo_children()[0]
        if platform.system() == "Windows" or platform.system() == "Darwin":
            child.bind_all("<MouseWheel>", lambda e: _on_mousewheel(e, child))
            child.bind_all("<Shift-MouseWheel>", lambda e: _on_shiftmouse(e, child))
        else:
            child.bind_all("<Button-4>", lambda e: _on_mousewheel(e, child))
            child.bind_all("<Button-5>", lambda e: _on_mousewheel(e, child))
            child.bind_all("<Shift-Button-4>", lambda e: _on_shiftmouse(e, child))
            child.bind_all("<Shift-Button-5>", lambda e: _on_shiftmouse(e, child))

    def _unbound_to_mousewheel(event, widget) -> None:
        if platform.system() == "Windows" or platform.system() == "Darwin":
            widget.unbind_all("<MouseWheel>")
            widget.unbind_all("<Shift-MouseWheel>")
        else:
            widget.unbind_all("<Button-4>")
            widget.unbind_all("<Button-5>")
            widget.unbind_all("<Shift-Button-4>")
            widget.unbind_all("<Shift-Button-5>")

    def _on_mousewheel(event, widget) -> None:
        if platform.system() == "Windows":
            widget.yview_scroll(-1 * int(event.delta / 120), "units")
        elif platform.system() == "Darwin":
            widget.yview_scroll(-1 * int(event.delta), "units")
        else:
            if event.num == 4:
                widget.yview_scroll(-1, "units")
            elif event.num == 5:
                widget.yview_scroll(1, "units")

    def _on_shiftmouse(event, widget) -> None:
        if platform.system() == "Windows":
            widget.xview_scroll(-1 * int(event.delta / 120), "units")
        elif platform.system() == "Darwin":
            widget.xview_scroll(-1 * int(event.delta), "units")
        else:
            if event.num == 4:
                widget.xview_scroll(-1, "units")
            elif event.num == 5:
                widget.xview_scroll(1, "units")

    class ScrolledText(Scroller, tk.Text):
        """Scrolled Text with SuperWidget mixin"""

        __desc__ = """Scrolled Text SuperWidget"""

        @_create_container
        def __init__(self, parent, widgetargs: dict = {}, **kw):
            tk.Text.__init__(
                self,
                parent,
                wrap=tk.WORD,
                **kw,
            )
            # Some systems don't bind this automatically
            self.bind("<Control-Key-a>", self.select_all, "+")
            Scroller.__init__(self, parent)
            # Create widget proxy
            self._orig = self._w + "_orig"
            self.tk.call("rename", self._w, self._orig)
            self.tk.createcommand(self._w, self._event_generate)

        def _event_generate(self, tk_call: str, *args) -> tk.Event:
            """Proxy method to generate an event when text contents change"""
            try:
                result = self.tk.call((self._orig, tk_call) + args)
            except Exception:
                return None
            if tk_call in ("insert", "delete", "replace"):
                self.event_generate("<<Modified>>")
            return result

        def select_all(self, event=None) -> None:
            """Selects all text. `Returns None`"""
            self.tag_add(tk.SEL, "1.0", tk.END)
            self.mark_set(tk.INSERT, "1.0")
            self.see(tk.INSERT)

        def set(self, val: str) -> None:
            """Sets the text. `Returns a String`"""
            state = self["state"]
            self.configure(state=tk.NORMAL)
            self.clear()
            self.insert("1.0", val)
            self.configure(state=state)

        def get(self, start: str = "1.0", end: str = tk.END):
            """Returns the contents of the text box with optional start/end kwargs. `Returns a String`"""
            return tk.Text.get(self, start, end)

        def clear(self) -> None:
            """Empties the text box. `Returns None`"""
            self.delete("1.0", tk.END)

        def get_cursor(self):
            """Get the current location of the cursor. `Returns None`"""
            return tk.Text.index(self, tk.INSERT)

        def set_cursor(self, col: int, row: int) -> None:
            """Sets the cursor to a given col / row. `Returns None`"""
            text_widget_name.mark_set(tk.INSERT, "%d.%d" % (col, row))

        def enable(self) -> None:
            """Enable Text box"""
            self.config(state="normal")

        def disable(self) -> None:
            self.config(state="disable")

    class CopyBox(ttk.Frame):
        """Scrolled Text with "Copy to Clipboard" Button"""

        __desc__ = "A widget with a scrolled textbox and button that copies the textbox contents to the user's clipboard. Useful for form output, etc."

        def __init__(self, parent: ttk.Frame, **kw):
            ttk.Frame.__init__(self, parent)
            self.button = ttk.Button(
                self, text="Copy to Clipboard", command=self._on_click
            )
            self.button.pack(side=tk.BOTTOM, fill="x", expand=False, pady=(0, 5))
            self.text = ScrolledText(self, **kw)
            self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def _on_click(self) -> None:
            self.button.configure(text="Copied!")
            self.clipboard_clear()
            self.clipboard_append(self.get())
            self.after(1000, lambda: self.button.configure(text="Copy To Clipboard"))

        def enable(self) -> None:
            """Enable CopyBox"""
            self.text.enable()

        def disable(self) -> None:
            """Disable CopyBox"""
            self.text.disable()

        def get(self) -> None:
            """Get CopyBox contents"""
            return self.text.get()

        def set(self, val: str) -> None:
            """Set CopyBox Contents"""
            self.text.set(val)

        def clear(self) -> None:
            """Clear CopyBox Contents"""
            self.text.clear()

    class TextToMorseTab(ttk.Frame):
        def __init__(self, parent: ttk.Frame):
            tk.Frame.__init__(self, parent)

            input_frame = ttk.LabelFrame(
                self, text="Text Input", style="Bold.TLabelframe"
            )
            input_frame.pack(fill="x", side="top", anchor="n", padx=10, pady=10)

            self.entry = ScrolledText(input_frame, height=2)
            self.entry.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=10
            )
            self.entry.bind("<<Modified>>", self.on_change, add="+")

            output_frame = ttk.LabelFrame(
                self, text="Outputs", style="Bold.TLabelframe"
            )
            output_frame.pack(
                side="top", fill="x", anchor="n", pady=(0, 10), padx=10, expand=True
            )

            #############
            out_frame = ttk.LabelFrame(output_frame, text="Morse")
            out_frame.pack(fill="x", expand=True, side="top", anchor="n", padx=10)
            self.output = CopyBox(out_frame, height=2)
            self.output.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=(0, 10)
            )
            self.output.text.disable()

            #############
            bits_frame = ttk.LabelFrame(output_frame, text="Bitstream Output")
            bits_frame.pack(fill="x", expand=True, side="top", anchor="n", padx=10)
            self.beats = CopyBox(bits_frame, height=2)
            self.beats.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=(0, 10)
            )
            self.beats.text.disable()

            #############
            visual_frame = ttk.LabelFrame(output_frame, text="Visual Output")
            visual_frame.pack(fill="x", expand=True, side="top", anchor="n", padx=10)
            self.visual = CopyBox(visual_frame, height=2)
            self.visual.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=(0, 10)
            )
            self.visual.text.disable()

            #############
            audio_frame = ttk.LabelFrame(output_frame, text="Audio Output")
            audio_frame.pack(fill="x", side="top", anchor="n", padx=10, pady=(0, 10))

            options_frame = ttk.Frame(audio_frame)
            options_frame.pack(fill="x", padx=10, pady=10)

            tone_frame = ttk.Frame(options_frame)
            tone_frame.pack(fill="x", padx=10, side="left")
            ttk.Label(tone_frame, text="Tone (Hz)").pack(fill="x", side="left")
            self.tone_var = tk.StringVar(value="800")
            ttk.Combobox(
                tone_frame,
                values=[i for i in range(800, 1500, 100)],
                textvariable=self.tone_var,
            ).pack(fill="x", expand=True, side="right")

            wpm_frame = ttk.Frame(options_frame)
            wpm_frame.pack(fill="x", side="right")
            ttk.Label(wpm_frame, text="Words Per Minute").pack(fill="x", side="left")
            self.duration_var = tk.StringVar(value="24")
            ttk.Combobox(
                wpm_frame,
                values=list(range(1, 31)),
                textvariable=self.duration_var,
            ).pack(fill="x", expand=True, padx=10, side="right")

            ttk.Button(audio_frame, text="Play", command=self.on_play).pack(
                fill="x", expand=False, anchor="n", padx=10, pady=(0, 10)
            )

            ttk.Button(audio_frame, text="Export", command=self.on_export).pack(
                fill="x", expand=False, anchor="n", padx=10, pady=(0, 10)
            )

        def on_change(self, event):
            morse = encode_string_to_morse(self.entry.get(), verbose=False)
            self.output.text.enable()
            self.output.set(morse.replace("  ", " / "))
            self.output.text.disable()

            beats = encode_morse_to_beats(morse, verbose=False)
            self.beats.text.enable()
            self.beats.set("".join([["0", "1"][b] for b in beats]))
            self.beats.text.disable()

            visual = make_morse_visual_from_beats(beats)
            self.visual.text.enable()
            self.visual.set(visual)
            self.visual.text.disable()

        def on_play(self) -> None:
            play(
                self.entry.get(),
                int(self.tone_var.get()),
                float(self.duration_var.get()),
            )

        def on_export(self) -> None:
            filetypes = [("Wave File", "*.wav")]
            filename = asksaveasfilename(
                filetypes=filetypes, defaultextension=filetypes
            )

            export(
                filename,
                self.entry.get(),
                int(self.tone_var.get()),
                float(self.duration_var.get()),
            )

    class MorseToTextTab(ttk.Frame):
        def __init__(self, parent: ttk.Frame):
            tk.Frame.__init__(self, parent)

            input_frame = ttk.LabelFrame(
                self, text="Morse Input", style="Bold.TLabelframe"
            )
            input_frame.pack(fill="x", side="top", anchor="n", padx=10, pady=10)
            self.entry = ScrolledText(input_frame, height=2)
            self.entry.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=10
            )
            self.entry.bind("<<Modified>>", self.on_change, add="+")

            output_frame = ttk.LabelFrame(self, text="Output", style="Bold.TLabelframe")
            output_frame.pack(fill="x", side="top", anchor="n", pady=(0, 10), padx=10)
            self.output = CopyBox(output_frame, height=2)
            self.output.pack(
                fill="both", expand=True, side="top", anchor="n", padx=10, pady=(0, 10)
            )
            self.output.text.disable()

        def on_change(self, event):
            text = decode_morse_to_string(self.entry.get())
            self.output.set(text)

    class LiveDecoderTab(ttk.Frame):
        def __init__(self, parent: ttk.Frame):
            tk.Frame.__init__(self, parent)

            self.signal_processor = SignalProcessor()
            self.decoder = MorseCodeTranslator(tolerance=2, words_per_minute=24)

            self.enabled = False
            self.enable_button_text_var = tk.StringVar(value="Enable")
            tk.Button(
                self, textvariable=self.enable_button_text_var, command=self.toggle
            ).pack(fill="x", expand=False, padx=10, pady=10)

            options_frame = ttk.Frame(self)
            options_frame.pack(fill="x", padx=10, pady=(0, 10))

            tone_frame = ttk.Frame(options_frame)
            tone_frame.pack(fill="x", padx=10, side="left")
            ttk.Label(tone_frame, text="Approximate Tone (Hz)").pack(
                fill="x", side="left"
            )
            self.tone_var = tk.StringVar(value="1000")
            tone_combobox = ttk.Combobox(
                tone_frame,
                values=[i for i in range(800, 1500, 100)],
                textvariable=self.tone_var,
            )
            tone_combobox.pack(fill="x", expand=True, side="right")
            tone_combobox.bind("<<ComboboxSelected>>", self.on_tone_change)

            wpm = ttk.Frame(options_frame)
            wpm.pack(fill="x", side="right")
            ttk.Label(wpm, text="Words Per Minute").pack(fill="x", side="left")
            self.wpm_var = tk.StringVar(value="24")
            wpm_combobox = ttk.Combobox(
                wpm,
                values=list(range(5, 31)),
                textvariable=self.wpm_var,
            )
            wpm_combobox.pack(fill="x", expand=True, padx=10, side="right")
            wpm_combobox.bind("<<ComboboxSelected>>", self.on_wpm_change)

            unparsed_frame = ttk.LabelFrame(self, text="Raw Input")
            unparsed_frame.pack(fill="both", expand=True, padx=10)
            self.unparsed_var = tk.StringVar()
            tk.Label(unparsed_frame, textvariable=self.unparsed_var).pack(
                fill="both", expand=True, side="top", anchor="center"
            )

            parsed_frame = ttk.LabelFrame(self, text="Decoded")
            parsed_frame.pack(fill="both", expand=True, padx=10)
            self.parsed_var = tk.StringVar()
            self.parsed_label = tk.Label(parsed_frame, textvariable=self.parsed_var)
            self.parsed_label.pack(
                fill="both", expand=True, side="top", anchor="center"
            )
            tk.Button(self, text="Reset", command=self.clear).pack(
                fill="x", expand=False, padx=10, pady=10
            )

            # Post setup
            self.on_tone_change()
            self.on_wpm_change()

        def toggle(self) -> None:
            self.enabled = not self.enabled
            self.enable_button_text_var.set(["Enable", "Disable"][self.enabled])

        def clear(self) -> None:
            self.decoder.unparsed_content = ""
            self.decoder.parsed_content = ""
            self.unparsed_var.set(self.decoder.unparsed_content)
            self.parsed_var.set(self.decoder.parsed_content)

        def update(self) -> None:
            self.decoder.update(self.signal_processor.process())
            self.unparsed_var.set(self.decoder.unparsed_content)
            self.parsed_var.set(self.decoder.parsed_content)

        def on_wpm_change(self, event=None) -> None:
            wpm = int(self.wpm_var.get())
            print(f"Decoder wpm set to {wpm}")
            self.decoder.words_per_minute = wpm

        def on_tone_change(self, event=None) -> None:
            tone = int(self.tone_var.get())
            print(f"Live processor signal tone set to {tone}")
            self.signal_processor.min_tone = tone - 400
            self.signal_processor.max_tone = tone + 400

    class UpdateThread(threading.Thread):
        def __init__(self, gui, *args, **kw):
            self.gui = gui
            threading.Thread.__init__(self, *args, **kw)

        def run(self) -> None:
            """Thread loop for keep gui updated"""
            try:
                self.gui.live_decoder_tab.signal_processor.start_session()  # open audio resources
                while True:
                    if self.gui.live_decoder_tab.enabled:
                        self.gui.live_decoder_tab.update()
                    else:
                        time.sleep(0.1)
            except KeyboardInterrupt:
                self.gui.live_decoder_tab.signal_processor.end_session()

    class GUI(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.title("Morse GUI")
            fnt = tkFont.nametofont("TkDefaultFont").actual()
            self.bold_font = (fnt["family"], fnt["size"], "bold")
            self.style = ttk.Style()
            self.style.theme_use("winnative")
            self.style.configure("Bold.TLabelframe.Label", font=self.bold_font)

            # Add all the tabs
            (notebook := ttk.Notebook(self)).pack(fill="x")
            notebook.add(TextToMorseTab(self), text="Text->Morse")
            notebook.add(MorseToTextTab(self), text="Morse->Text")
            self.live_decoder_tab = LiveDecoderTab(self)  # Needed by update thread
            notebook.add(self.live_decoder_tab, text="Live Decoder")

    gui = GUI()
    UpdateThread(gui).start()
    gui.mainloop()
