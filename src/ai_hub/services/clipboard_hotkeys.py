"""
Clipboard Hotkey Service

Registers hotkeys for clipboard items dynamically.
"""

from __future__ import annotations

import keyboard
from typing import Dict, Callable, Optional

from .clipboard_manager import ClipboardManager


class ClipboardHotkeyService:
    """Manages hotkeys for clipboard items."""
    
    def __init__(self, manager: ClipboardManager):
        self.manager = manager
        self.registered_hotkeys: Dict[str, str] = {}  # hotkey -> item_id
    
    def register_all(self) -> None:
        """Register hotkeys for all items that have them."""
        self.unregister_all()
        
        for item in self.manager.items:
            if item.hotkey:
                self.register_hotkey(item.id, item.hotkey)
    
    def register_hotkey(self, item_id: str, hotkey: str) -> bool:
        """Register a hotkey for an item."""
        try:
            # Create handler that copies item to clipboard
            def handler():
                self.manager.copy_to_clipboard(item_id)
                print(f"📋 Clipboard hotkey triggered: {hotkey}")
            
            keyboard.add_hotkey(hotkey, handler, suppress=False, trigger_on_release=True)
            self.registered_hotkeys[hotkey] = item_id
            print(f"✅ Registered clipboard hotkey: {hotkey}")
            return True
            
        except Exception as e:
            print(f"⚠️ Error registering clipboard hotkey {hotkey}: {e}")
            return False
    
    def unregister_hotkey(self, hotkey: str) -> bool:
        """Unregister a hotkey."""
        try:
            keyboard.remove_hotkey(hotkey)
            if hotkey in self.registered_hotkeys:
                del self.registered_hotkeys[hotkey]
            return True
        except Exception:
            return False
    
    def unregister_all(self) -> None:
        """Unregister all clipboard hotkeys."""
        for hotkey in list(self.registered_hotkeys.keys()):
            self.unregister_hotkey(hotkey)
    
    def refresh(self) -> None:
        """Refresh all hotkeys (re-register based on current items)."""
        self.register_all()
