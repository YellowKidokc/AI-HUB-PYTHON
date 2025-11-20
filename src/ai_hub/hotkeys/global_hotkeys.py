from __future__ import annotations

import json
import subprocess
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import keyboard

from ..services.openai_client import OpenAIClient
from ..services.prompt_manager import Prompt
from ..services.selection import get_selection, replace_selection
from ..ui.dialogs.prompt_navigator import PromptNavigator
from ..ui.dialogs.result_popup import ResultPopup


@dataclass(slots=True)
class HotkeyCallbacks:
    focus_hub_tab: Callable[[], None]


class GlobalHotkeys:
    def __init__(
        self,
        client: OpenAIClient,
        prompts: list[Prompt],
        spelling_prompt: Prompt,
        callbacks: HotkeyCallbacks,
        prompt_hotkey: str,
        spelling_hotkey: str,
        goto_hotkey: str | None,
    ) -> None:
        self._client = client
        self._prompts = prompts
        self._spelling_prompt = spelling_prompt
        self._callbacks = callbacks
        self._prompt_hotkey = prompt_hotkey
        self._spelling_hotkey = spelling_hotkey
        self._goto_hotkey = goto_hotkey
        self._navigator = PromptNavigator(client, prompts)

    def start(self) -> None:
        # Register default hotkeys
        keyboard.add_hotkey(self._spelling_hotkey, self._run_spelling, suppress=False, trigger_on_release=True)
        keyboard.add_hotkey(self._prompt_hotkey, self._show_prompt_navigator, suppress=False, trigger_on_release=True)
        if self._goto_hotkey:
            keyboard.add_hotkey(self._goto_hotkey, self._callbacks.focus_hub_tab, suppress=False, trigger_on_release=True)
        
        # Load and register custom shortcuts from JSON
        self._load_custom_shortcuts()

    def _show_prompt_navigator(self) -> None:
        self._navigator.show_near_cursor()

    def _run_spelling(self) -> None:
        selection = get_selection().text
        if not selection.strip():
            return

        def run() -> None:
            output = self._client.chat(self._spelling_prompt.system or None, self._spelling_prompt.build_message(selection), self._spelling_prompt.temperature)
            if output.strip():
                replace_selection(output)

        threading.Thread(target=run, daemon=True).start()

    def run_prompt_by_index(self, index: int) -> None:
        if index < 0 or index >= len(self._prompts):
            return
        prompt = self._prompts[index]
        selection = get_selection().text
        if not selection.strip():
            return

        def run() -> None:
            output = self._client.chat(prompt.system or None, prompt.build_message(selection), prompt.temperature)
            if not output.strip():
                return
            if prompt.replace:
                replace_selection(output)
            else:
                ResultPopup.show_text(prompt.name, output)

        threading.Thread(target=run, daemon=True).start()

    def _load_custom_shortcuts(self) -> None:
        """Load custom shortcuts from JSON and register them."""
        shortcuts_file = Path("config/shortcuts.json")
        if not shortcuts_file.exists():
            return

        try:
            with open(shortcuts_file, "r", encoding="utf-8") as f:
                shortcuts = json.load(f)

            for shortcut in shortcuts:
                if shortcut["type"] == "Hotkey":
                    self._register_hotkey(shortcut)
                elif shortcut["type"] == "Hotstring":
                    self._register_hotstring(shortcut)

            print(f"✅ Loaded {len(shortcuts)} custom shortcuts")
        except Exception as e:
            print(f"⚠️ Error loading custom shortcuts: {e}")

    def _register_hotkey(self, shortcut: dict[str, Any]) -> None:
        """Register a custom hotkey."""
        try:
            # Build the hotkey string (e.g., "ctrl+alt+k")
            modifiers = shortcut.get("modifiers", [])
            trigger = shortcut["trigger"]
            hotkey_str = "+".join(modifiers + [trigger]) if modifiers else trigger

            # Create the handler based on action type
            action = shortcut["action"]
            if action == "Send Text":
                handler = self._make_send_text_handler(shortcut["output"])
            elif action == "Run Program":
                handler = self._make_run_program_handler(shortcut["output"])
            elif action == "AI Rewrite":
                handler = self._make_ai_rewrite_handler(shortcut["output"])
            elif action == "Mouse Click":
                handler = self._make_mouse_click_handler(shortcut["output"])
            else:
                return

            keyboard.add_hotkey(hotkey_str, handler, suppress=False, trigger_on_release=True)
            print(f"✅ Registered hotkey: {hotkey_str} -> {action}")
        except Exception as e:
            print(f"⚠️ Error registering hotkey {shortcut.get('trigger')}: {e}")

    def _register_hotstring(self, shortcut: dict[str, Any]) -> None:
        """Register a custom hotstring (text replacement)."""
        # Note: Hotstrings are handled by the HotstringEngine in main_window.py
        # This is a placeholder for future integration
        pass

    def _make_send_text_handler(self, text: str) -> Callable[[], None]:
        """Create a handler that sends text."""
        def handler() -> None:
            keyboard.write(text)
        return handler

    def _make_run_program_handler(self, program_path: str) -> Callable[[], None]:
        """Create a handler that runs a program."""
        def handler() -> None:
            try:
                subprocess.Popen(program_path, shell=True)
            except Exception as e:
                print(f"⚠️ Error running program: {e}")
        return handler

    def _make_ai_rewrite_handler(self, instruction: str) -> Callable[[], None]:
        """Create a handler that uses AI to rewrite selected text."""
        def handler() -> None:
            selection = get_selection().text
            if not selection.strip():
                return

            def run() -> None:
                try:
                    # Use the instruction as the user message
                    system_msg = "You are a helpful writing assistant. Follow the user's instructions precisely."
                    user_msg = f"{instruction}\n\nText to process:\n{selection}"
                    output = self._client.chat(system_msg, user_msg, temperature=0.7)
                    if output.strip():
                        replace_selection(output)
                except Exception as e:
                    print(f"⚠️ AI rewrite error: {e}")

            threading.Thread(target=run, daemon=True).start()

        return handler

    def _make_mouse_click_handler(self, position_str: str) -> Callable[[], None]:
        """Create a handler that clicks at a specific position."""
        def handler() -> None:
            try:
                # Parse position string (e.g., "100, 200")
                parts = position_str.split(',')
                if len(parts) != 2:
                    print(f"⚠️ Invalid mouse position format: {position_str}")
                    return
                
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                
                # Import and use mouse automation
                from ..services.mouse_automation import quick_click
                
                # Click in background thread (double-click for mic toggle)
                def click_thread():
                    success = quick_click(x, y, clicks=2)  # Double-click
                    if success:
                        print(f"🖱️ Double-clicked at ({x}, {y})")
                    else:
                        print(f"❌ Click failed at ({x}, {y})")
                
                threading.Thread(target=click_thread, daemon=True).start()
                
            except Exception as e:
                print(f"⚠️ Mouse click error: {e}")
        
        return handler
