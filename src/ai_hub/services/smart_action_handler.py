"""Smart action handler for your workflow - select all, rewrite, paste back."""

from __future__ import annotations

import subprocess
from typing import Callable

from .openai_client import OpenAIClient
from .text_selector import TextSelector


class SmartActionHandler:
    """Handles your specific workflow: select all → rewrite → paste back."""

    def __init__(self, client: OpenAIClient):
        self._client = client
        self._text_selector = TextSelector()

    def rewrite_all_in_window(self, on_progress: Callable[[str], None] = None) -> bool:
        """
        Your main workflow for Alt+Spacebar:
        1. Select all text in window
        2. Rewrite for clarity (keep tone/voice)
        3. Paste back to window
        4. If paste fails, open notepad and paste there
        """
        try:
            # Step 1: Select all text
            if on_progress:
                on_progress("Selecting all text...")
            text = self._text_selector.select_all_in_window()

            if not text or text.strip() == "":
                if on_progress:
                    on_progress("No text found to rewrite")
                return False

            original_text = text

            # Step 2: Rewrite for clarity
            if on_progress:
                on_progress("Rewriting for clarity...")

            rewrite_prompt = """Rewrite this text to be clearer and more readable while keeping the original tone, voice, and meaning. 
Remove filler words like "um", "and", "uh", etc. 
Fix any grammatical issues.
Improve sentence structure for clarity.
Return ONLY the rewritten text, nothing else."""

            rewritten_text = self._client.chat(
                system=rewrite_prompt, user=text, temperature=0.3
            )

            if on_progress:
                on_progress("Pasting back to window...")

            # Step 3: Try to paste back to original window
            success = self._text_selector.paste_to_window(rewritten_text)

            if success:
                if on_progress:
                    on_progress("Done! Text rewritten and pasted.")
                return True
            else:
                # Step 4: If paste failed, open notepad
                if on_progress:
                    on_progress("Opening notepad to paste result...")
                return self._paste_to_notepad(rewritten_text)

        except Exception as e:
            if on_progress:
                on_progress(f"Error: {str(e)}")
            return False

    def execute_prompt_on_selected(
        self, prompt: dict, on_progress: Callable[[str], None] = None
    ) -> tuple[bool, str]:
        """
        Your Ctrl+Alt+Spacebar workflow:
        1. Get selected text (or select all)
        2. Apply chosen prompt
        3. Return result
        """
        try:
            # Get selected text
            if on_progress:
                on_progress(f"Processing with {prompt.get('name', 'prompt')}...")

            # Try clipboard first
            text = self._text_selector.get_selected_text()

            if not text or text.strip() == "":
                # If nothing in clipboard, select all
                if on_progress:
                    on_progress("No selection found. Selecting all text...")
                text = self._text_selector.select_all_in_window()

            if not text or text.strip() == "":
                if on_progress:
                    on_progress("No text found")
                return False, ""

            # Apply prompt
            if on_progress:
                on_progress(f"Executing prompt...")

            result = self._client.chat(
                system=prompt.get("prompt", ""), user=text, temperature=0.2
            )

            if on_progress:
                on_progress("Done!")

            return True, result

        except Exception as e:
            if on_progress:
                on_progress(f"Error: {str(e)}")
            return False, ""

    @staticmethod
    def _paste_to_notepad(text: str) -> bool:
        """
        Open Notepad and paste the text there.
        This is your fallback if paste-back fails.
        """
        try:
            # Copy to clipboard
            TextSelector.copy_text_to_clipboard(text)

            # Open notepad
            subprocess.Popen("notepad.exe")

            # Wait a bit for notepad to open
            import time

            time.sleep(0.5)

            # Paste (Ctrl+V)
            import pynput.keyboard as keyboard

            controller = keyboard.Controller()
            with controller.pressed(keyboard.Key.ctrl):
                controller.press(keyboard.Key.v)
                controller.release(keyboard.Key.v)

            return True
        except Exception as e:
            print(f"Error opening notepad: {e}")
            return False

