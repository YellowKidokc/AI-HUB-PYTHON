"""
Clipboard Manager Service

Monitors clipboard, saves history, supports pinning and hotkeys.
"""

from __future__ import annotations

import json
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, Callable, List

import pyperclip


@dataclass
class ClipboardItem:
    """A clipboard history item."""
    id: str
    content: str
    timestamp: str
    pinned: bool = False
    hotkey: Optional[str] = None
    label: Optional[str] = None
    
    @staticmethod
    def create(content: str) -> ClipboardItem:
        """Create a new clipboard item."""
        # Generate unique ID from content hash
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        timestamp = datetime.now().isoformat()
        return ClipboardItem(
            id=f"{content_hash}_{timestamp}",
            content=content,
            timestamp=timestamp
        )
    
    def preview(self, max_length: int = 100) -> str:
        """Get a preview of the content."""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    @staticmethod
    def from_dict(data: dict) -> ClipboardItem:
        """Create from dictionary."""
        return ClipboardItem(**data)


class ClipboardManager:
    """Manages clipboard history with persistence."""
    
    def __init__(self, storage_path: Path, max_history: int = 100):
        self.storage_path = storage_path
        self.max_history = max_history
        self.items: List[ClipboardItem] = []
        self.on_new_item: Optional[Callable[[ClipboardItem], None]] = None
        self._last_content: Optional[str] = None
        
        # Load existing history
        self.load()
    
    def load(self) -> None:
        """Load clipboard history from disk."""
        if not self.storage_path.exists():
            return
        
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.items = [ClipboardItem.from_dict(item) for item in data]
            print(f"✅ Loaded {len(self.items)} clipboard items")
        except Exception as e:
            print(f"⚠️ Error loading clipboard history: {e}")
            self.items = []
    
    def save(self) -> None:
        """Save clipboard history to disk."""
        try:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                data = [item.to_dict() for item in self.items]
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error saving clipboard history: {e}")
    
    def add_item(self, content: str, auto_save: bool = True) -> Optional[ClipboardItem]:
        """Add a new clipboard item."""
        # Skip empty content
        if not content or not content.strip():
            return None
        
        # Skip if same as last item
        if self.items and self.items[0].content == content:
            return None
        
        # Create new item
        item = ClipboardItem.create(content)
        
        # Add to beginning of list
        self.items.insert(0, item)
        
        # Remove old unpinned items if over limit
        unpinned_count = sum(1 for i in self.items if not i.pinned)
        if unpinned_count > self.max_history:
            # Remove oldest unpinned items
            for i in range(len(self.items) - 1, -1, -1):
                if not self.items[i].pinned:
                    self.items.pop(i)
                    unpinned_count -= 1
                    if unpinned_count <= self.max_history:
                        break
        
        # Save to disk
        if auto_save:
            self.save()
        
        # Notify listeners
        if self.on_new_item:
            self.on_new_item(item)
        
        return item
    
    def check_clipboard(self) -> Optional[ClipboardItem]:
        """Check clipboard for new content."""
        try:
            content = pyperclip.paste()
            
            # Skip if same as last check
            if content == self._last_content:
                return None
            
            self._last_content = content
            
            # Add to history
            return self.add_item(content)
            
        except Exception as e:
            print(f"⚠️ Error checking clipboard: {e}")
            return None
    
    def get_item_by_id(self, item_id: str) -> Optional[ClipboardItem]:
        """Get item by ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def toggle_pin(self, item_id: str) -> bool:
        """Toggle pin status of an item."""
        item = self.get_item_by_id(item_id)
        if item:
            item.pinned = not item.pinned
            self.save()
            return item.pinned
        return False
    
    def set_hotkey(self, item_id: str, hotkey: Optional[str]) -> bool:
        """Set hotkey for an item."""
        item = self.get_item_by_id(item_id)
        if item:
            item.hotkey = hotkey
            self.save()
            return True
        return False
    
    def set_label(self, item_id: str, label: Optional[str]) -> bool:
        """Set label for an item."""
        item = self.get_item_by_id(item_id)
        if item:
            item.label = label
            self.save()
            return True
        return False
    
    def delete_item(self, item_id: str) -> bool:
        """Delete an item."""
        item = self.get_item_by_id(item_id)
        if item and not item.pinned:
            self.items.remove(item)
            self.save()
            return True
        return False
    
    def copy_to_clipboard(self, item_id: str) -> bool:
        """Copy an item to clipboard."""
        item = self.get_item_by_id(item_id)
        if item:
            try:
                pyperclip.copy(item.content)
                return True
            except Exception as e:
                print(f"⚠️ Error copying to clipboard: {e}")
        return False
    
    def clear_unpinned(self) -> int:
        """Clear all unpinned items."""
        count = len([i for i in self.items if not i.pinned])
        self.items = [i for i in self.items if i.pinned]
        self.save()
        return count
    
    def get_pinned_items(self) -> List[ClipboardItem]:
        """Get all pinned items."""
        return [i for i in self.items if i.pinned]
    
    def get_recent_items(self, limit: int = 50) -> List[ClipboardItem]:
        """Get recent items (unpinned)."""
        unpinned = [i for i in self.items if not i.pinned]
        return unpinned[:limit]
