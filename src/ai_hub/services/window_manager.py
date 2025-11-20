"""
Window Manager Service

Manages window positions, sizes, and always-on-top settings.
Persists settings across sessions.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class WindowSettings:
    """Manages window settings persistence."""

    def __init__(self, settings_file: str = "config/window_settings.json"):
        self.settings_file = Path(settings_file)
        self.settings: dict[str, Any] = {}
        self._load_settings()

    def _load_settings(self) -> None:
        """Load settings from file."""
        if self.settings_file.exists():
            try:
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    self.settings = json.load(f)
                print(f"✅ Loaded window settings from {self.settings_file}")
            except Exception as e:
                print(f"⚠️ Could not load window settings: {e}")
                self.settings = {}
        else:
            # Create default settings
            self.settings = {
                "main_window": {
                    "x": 100,
                    "y": 100,
                    "width": 1000,
                    "height": 720,
                    "always_on_top": False
                },
                "floating_player": {
                    "x": -1,  # -1 means auto-position
                    "y": -1,
                    "width": 200,
                    "height": 120,
                    "always_on_top": True
                },
                "global_always_on_top": False
            }
            self._save_settings()

    def _save_settings(self) -> None:
        """Save settings to file."""
        try:
            # Ensure directory exists
            self.settings_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.settings_file, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2)
            print(f"💾 Saved window settings to {self.settings_file}")
        except Exception as e:
            print(f"⚠️ Could not save window settings: {e}")

    def get_window_settings(self, window_name: str) -> dict[str, Any]:
        """Get settings for a specific window."""
        return self.settings.get(window_name, {})

    def save_window_position(self, window_name: str, x: int, y: int) -> None:
        """Save window position."""
        if window_name not in self.settings:
            self.settings[window_name] = {}
        
        self.settings[window_name]["x"] = x
        self.settings[window_name]["y"] = y
        self._save_settings()

    def save_window_size(self, window_name: str, width: int, height: int) -> None:
        """Save window size."""
        if window_name not in self.settings:
            self.settings[window_name] = {}
        
        self.settings[window_name]["width"] = width
        self.settings[window_name]["height"] = height
        self._save_settings()

    def save_window_geometry(self, window_name: str, x: int, y: int, width: int, height: int) -> None:
        """Save complete window geometry."""
        if window_name not in self.settings:
            self.settings[window_name] = {}
        
        self.settings[window_name].update({
            "x": x,
            "y": y,
            "width": width,
            "height": height
        })
        self._save_settings()

    def set_always_on_top(self, window_name: str, enabled: bool) -> None:
        """Set always-on-top for a specific window."""
        if window_name not in self.settings:
            self.settings[window_name] = {}
        
        self.settings[window_name]["always_on_top"] = enabled
        self._save_settings()

    def set_global_always_on_top(self, enabled: bool) -> None:
        """Set global always-on-top for all windows."""
        self.settings["global_always_on_top"] = enabled
        self._save_settings()

    def get_global_always_on_top(self) -> bool:
        """Get global always-on-top setting."""
        return self.settings.get("global_always_on_top", False)

    def is_always_on_top(self, window_name: str) -> bool:
        """Check if window should be always on top."""
        # Global setting overrides individual
        if self.get_global_always_on_top():
            return True
        
        window_settings = self.get_window_settings(window_name)
        return window_settings.get("always_on_top", False)


# Global instance
_window_settings: WindowSettings | None = None


def get_window_settings() -> WindowSettings:
    """Get global window settings instance."""
    global _window_settings
    if _window_settings is None:
        _window_settings = WindowSettings()
    return _window_settings
