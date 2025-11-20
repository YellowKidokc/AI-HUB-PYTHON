"""
Global TTS Hotkey Service

Allows instant text-to-speech from any app using a hotkey.
Select text → Press hotkey → AI speaks it!
"""

from __future__ import annotations

import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .audio_engine import AudioEngine
    from ..ui.widgets.floating_player import FloatingPlayer

from .selection import get_selection


class TTSHotkeyService:
    """Service for global TTS hotkey."""

    def __init__(self, audio_engine: AudioEngine, floating_player: FloatingPlayer | None = None):
        self.audio_engine = audio_engine
        self.floating_player = floating_player

    def speak_selection(self) -> None:
        """
        Get selected text, copy it to clipboard, and speak it.
        This is the function called by the hotkey.
        """
        import pyperclip
        
        # Get selected text
        selection = get_selection().text
        
        if not selection or not selection.strip():
            print("⚠️ No text selected for TTS")
            # Optionally speak a message
            if self.audio_engine:
                threading.Thread(
                    target=lambda: self.audio_engine.speak("No text selected"),
                    daemon=True
                ).start()
            return

        # Auto-copy to clipboard
        try:
            pyperclip.copy(selection)
            print(f"📋 Copied to clipboard: {selection[:50]}...")
        except Exception as e:
            print(f"⚠️ Could not copy to clipboard: {e}")

        print(f"🔊 Speaking: {selection[:50]}...")
        
        # Show floating player if available
        if self.floating_player:
            self.floating_player.set_speaking(selection[:50] + "..." if len(selection) > 50 else selection)

        # Speak in background thread
        def speak_thread():
            try:
                success = self.audio_engine.speak(selection)
                if success:
                    print("✅ TTS complete")
                else:
                    print("❌ TTS failed")
            except Exception as e:
                print(f"❌ TTS error: {e}")

        threading.Thread(target=speak_thread, daemon=True).start()

    def set_floating_player(self, player: FloatingPlayer) -> None:
        """Set the floating player reference."""
        self.floating_player = player
