"""Hotkey handler for Prompt Selector - Ctrl+Alt+T."""

from __future__ import annotations

import keyboard
from typing import Optional, Callable


class PromptSelectorHotkey:
    """Manages Ctrl+Alt+T hotkey for opening prompt selector."""

    def __init__(self, on_show: Callable[[], None] = None):
        """Initialize hotkey handler."""
        self._on_show = on_show
        self._is_registered = False

    def start(self) -> None:
        """Start listening for Ctrl+Alt+T."""
        try:
            keyboard.add_hotkey("ctrl+alt+t", self._on_hotkey)
            self._is_registered = True
        except Exception as e:
            print(f"Error registering prompt selector hotkey: {e}")

    def stop(self) -> None:
        """Stop listening for hotkey."""
        try:
            keyboard.remove_hotkey("ctrl+alt+t")
            self._is_registered = False
        except Exception:
            pass

    def _on_hotkey(self) -> None:
        """Handle hotkey press."""
        if self._on_show:
            self._on_show()


