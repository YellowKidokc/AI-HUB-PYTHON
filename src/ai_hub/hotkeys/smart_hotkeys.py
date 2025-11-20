"""Smart hotkeys for your specific workflow."""

from __future__ import annotations

import keyboard
from typing import Callable

from ..services.openai_client import OpenAIClient
from ..services.smart_action_handler import SmartActionHandler
from ..ui.popups.floating_popup import FloatingPopup
from ..ui.popups.prompt_selector import PromptSelector


class SmartHotkeys:
    """Your custom hotkeys: Alt+Spacebar and Ctrl+Alt+Spacebar."""

    def __init__(
        self,
        client: OpenAIClient,
        prompts: list[dict] = None,
        on_show_progress: Callable[[str], None] = None,
    ):
        self._client = client
        self._handler = SmartActionHandler(client)
        self._prompts = prompts or self._get_default_prompts()
        self._on_show_progress = on_show_progress or self._default_progress

        self._is_processing = False

    def start(self) -> None:
        """Start listening for hotkeys."""
        # Alt+Spacebar: Rewrite all text in window
        keyboard.add_hotkey("alt+space", self._on_alt_spacebar)

        # Ctrl+Alt+Spacebar: Show prompt selector
        keyboard.add_hotkey("ctrl+alt+space", self._on_ctrl_alt_spacebar)

    def stop(self) -> None:
        """Stop listening for hotkeys."""
        keyboard.remove_hotkey("alt+space")
        keyboard.remove_hotkey("ctrl+alt+space")

    def _on_alt_spacebar(self) -> None:
        """
        Alt+Spacebar: Select all → Rewrite for clarity → Paste back.
        This is your main workflow!
        """
        if self._is_processing:
            return

        self._is_processing = True

        try:
            # Show progress window
            popup = FloatingPopup(
                title="AI Hub - Rewriting...",
                original_text="Processing your text...",
                result_text="Please wait while I rewrite your text for clarity.",
            )
            popup.show()

            # Do the work
            success = self._handler.rewrite_all_in_window(
                on_progress=lambda msg: self._update_popup(popup, msg)
            )

            if success:
                popup.setWindowTitle("AI Hub - Done!")
            else:
                popup.setWindowTitle("AI Hub - Done (check notepad)")

        except Exception as e:
            print(f"Error in Alt+Spacebar: {e}")
        finally:
            self._is_processing = False

    def _on_ctrl_alt_spacebar(self) -> None:
        """
        Ctrl+Alt+Spacebar: Show prompt manager.
        User selects a prompt, then execute it on selected text.
        """
        if self._is_processing:
            return

        self._is_processing = True

        try:
            # Show prompt selector
            def on_prompt_selected(prompt):
                self._execute_selected_prompt(prompt)

            selector = PromptSelector(self._prompts, on_select=on_prompt_selected)
            selector.show()

        except Exception as e:
            print(f"Error in Ctrl+Alt+Spacebar: {e}")
        finally:
            self._is_processing = False

    def _execute_selected_prompt(self, prompt: dict) -> None:
        """Execute the selected prompt on text."""
        try:
            success, result = self._handler.execute_prompt_on_selected(
                prompt, on_progress=self._on_show_progress
            )

            if success and result:
                # Show result in floating popup
                popup = FloatingPopup(
                    title=f"AI Hub - {prompt.get('name', 'Result')}",
                    result_text=result,
                )
                popup.show()

        except Exception as e:
            print(f"Error executing prompt: {e}")

    @staticmethod
    def _update_popup(popup, message: str) -> None:
        """Update popup with progress message."""
        if popup:
            popup._result_text_edit.setText(message)

    @staticmethod
    def _default_progress(message: str) -> None:
        """Default progress handler."""
        print(f"[AI Hub] {message}")

    @staticmethod
    def _get_default_prompts() -> list[dict]:
        """Get default prompts."""
        return [
            {
                "name": "Rewrite for Clarity",
                "description": "Rewrite to be clearer and more readable",
                "prompt": "Rewrite this text to be clearer and more readable while keeping the original tone and meaning. Remove filler words. Fix grammar.",
            },
            {
                "name": "Make Professional",
                "description": "Use a formal, professional tone",
                "prompt": "Rewrite this text in a formal, professional tone. Return ONLY the rewritten text.",
            },
            {
                "name": "Make Friendly",
                "description": "Use a casual, friendly tone",
                "prompt": "Rewrite this text in a casual, friendly tone. Return ONLY the rewritten text.",
            },
            {
                "name": "Summarize",
                "description": "Create a concise summary",
                "prompt": "Create a concise summary of this text. Return ONLY the summary.",
            },
            {
                "name": "Expand",
                "description": "Add more detail and explanations",
                "prompt": "Expand this text with more details and examples. Return ONLY the expanded text.",
            },
            {
                "name": "Fix Grammar",
                "description": "Fix all grammar and spelling errors",
                "prompt": "Fix all grammar, spelling, and punctuation errors. Return ONLY the corrected text.",
            },
            {
                "name": "Remove Filler",
                "description": "Remove um, uh, and other filler words",
                "prompt": "Remove all filler words like 'um', 'uh', 'and', 'like', etc. Keep the meaning. Return ONLY the cleaned text.",
            },
        ]

