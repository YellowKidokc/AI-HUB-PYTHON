"""
Mouse Automation Service

Automate mouse clicks at specific screen positions.
Perfect for toggling mic, clicking buttons, etc.
"""

from __future__ import annotations

import time
from typing import Tuple

try:
    import pyautogui
    HAVE_PYAUTOGUI = True
except ImportError:
    HAVE_PYAUTOGUI = False
    print("⚠️ pyautogui not installed. Run: pip install pyautogui")


class MouseAutomation:
    """Service for automating mouse clicks."""

    def __init__(self):
        if not HAVE_PYAUTOGUI:
            raise ImportError("pyautogui is required for mouse automation")
        
        # Safety: Fail-safe - move mouse to corner to abort
        pyautogui.FAILSAFE = True
        
        # Speed settings
        pyautogui.PAUSE = 0.1  # Small pause between actions
        
    def get_current_position(self) -> Tuple[int, int]:
        """Get current mouse position."""
        if not HAVE_PYAUTOGUI:
            return (0, 0)
        
        x, y = pyautogui.position()
        return (x, y)

    def click_at(self, x: int, y: int, clicks: int = 1, button: str = 'left', 
                 return_to_original: bool = True) -> bool:
        """
        Click at specific screen coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            clicks: Number of clicks (1 for single, 2 for double)
            button: 'left', 'right', or 'middle'
            return_to_original: Return mouse to original position after click
            
        Returns:
            True if successful, False otherwise
        """
        if not HAVE_PYAUTOGUI:
            print("⚠️ pyautogui not available")
            return False
        
        try:
            # Save original position
            original_x, original_y = self.get_current_position()
            
            # Move and click
            pyautogui.click(x, y, clicks=clicks, button=button)
            
            # Return to original position if requested
            if return_to_original:
                time.sleep(0.01)  # Tiny delay
                pyautogui.moveTo(original_x, original_y, duration=0.0)  # Instant return
            
            print(f"🖱️ Clicked at ({x}, {y}) - {clicks} {button} click(s)")
            return True
            
        except Exception as e:
            print(f"❌ Click failed: {e}")
            return False

    def click_sequence(self, positions: list[Tuple[int, int, int]], 
                      return_to_original: bool = True) -> bool:
        """
        Click multiple positions in sequence.
        
        Args:
            positions: List of (x, y, clicks) tuples
            return_to_original: Return to original position after all clicks
            
        Returns:
            True if all clicks successful
        """
        if not HAVE_PYAUTOGUI:
            return False
        
        try:
            # Save original position
            original_x, original_y = self.get_current_position()
            
            # Click each position
            for x, y, clicks in positions:
                pyautogui.click(x, y, clicks=clicks)
                time.sleep(0.1)  # Small delay between clicks
            
            # Return to original position
            if return_to_original:
                time.sleep(0.01)
                pyautogui.moveTo(original_x, original_y, duration=0.0)  # Instant return
            
            print(f"🖱️ Clicked {len(positions)} positions")
            return True
            
        except Exception as e:
            print(f"❌ Click sequence failed: {e}")
            return False

    def toggle_at_position(self, x: int, y: int, clicks: int = 1) -> bool:
        """
        Toggle something at a position (like a mic button).
        Clicks and returns to original position.
        
        Args:
            x: X coordinate
            y: Y coordinate
            clicks: Number of clicks (usually 1)
            
        Returns:
            True if successful
        """
        return self.click_at(x, y, clicks=clicks, button='left', return_to_original=True)

    def get_screen_size(self) -> Tuple[int, int]:
        """Get screen size."""
        if not HAVE_PYAUTOGUI:
            return (1920, 1080)  # Default
        
        return pyautogui.size()


# Quick helper functions
def quick_click(x: int, y: int, clicks: int = 1) -> bool:
    """Quick click at position."""
    try:
        mouse = MouseAutomation()
        return mouse.click_at(x, y, clicks=clicks)
    except Exception as e:
        print(f"❌ Quick click failed: {e}")
        return False


def toggle_mic(x: int, y: int) -> bool:
    """Quick mic toggle at position."""
    try:
        mouse = MouseAutomation()
        return mouse.toggle_at_position(x, y, clicks=1)
    except Exception as e:
        print(f"❌ Mic toggle failed: {e}")
        return False


def get_mouse_position() -> Tuple[int, int]:
    """Get current mouse position."""
    if HAVE_PYAUTOGUI:
        return pyautogui.position()
    return (0, 0)
