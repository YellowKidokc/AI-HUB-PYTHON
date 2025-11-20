"""Text selection and clipboard management."""

from __future__ import annotations

import pyperclip
import time
from typing import Optional


class TextSelector:
    """Handles text selection and clipboard operations."""

    @staticmethod
    def get_selected_text() -> str:
        """Get currently selected text from clipboard."""
        try:
            # Try to get from clipboard (Ctrl+C copies selection)
            return pyperclip.paste()
        except Exception:
            return ""

    @staticmethod
    def select_all_in_window() -> str:
        """
        Select all text in the current window.
        
        Does:
        1. Sends Ctrl+A to select all
        2. Sends Ctrl+C to copy
        3. Waits for clipboard
        4. Returns selected text
        """
        try:
            import pynput.keyboard as keyboard
            
            controller = keyboard.Controller()
            
            # Select all (Ctrl+A)
            with controller.pressed(keyboard.Key.ctrl):
                controller.press(keyboard.Key.a)
                controller.release(keyboard.Key.a)
            
            time.sleep(0.1)  # Wait for selection
            
            # Copy (Ctrl+C)
            with controller.pressed(keyboard.Key.ctrl):
                controller.press(keyboard.Key.c)
                controller.release(keyboard.Key.c)
            
            time.sleep(0.2)  # Wait for copy
            
            # Get from clipboard
            text = pyperclip.paste()
            return text
        except Exception as e:
            print(f"Error selecting all text: {e}")
            return ""

    @staticmethod
    def paste_to_window(text: str) -> bool:
        """
        Paste text back to the current window.
        
        Does:
        1. Puts text in clipboard
        2. Sends Ctrl+V to paste
        3. Returns success
        """
        try:
            import pynput.keyboard as keyboard
            
            # Put text in clipboard
            pyperclip.copy(text)
            time.sleep(0.1)
            
            controller = keyboard.Controller()
            
            # Paste (Ctrl+V)
            with controller.pressed(keyboard.Key.ctrl):
                controller.press(keyboard.Key.v)
                controller.release(keyboard.Key.v)
            
            return True
        except Exception as e:
            print(f"Error pasting text: {e}")
            return False

    @staticmethod
    def copy_text_to_clipboard(text: str) -> bool:
        """Copy text to clipboard."""
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            return False

