"""
Position Recorder Widget

Helps record mouse positions for automation.
Shows current position and lets you save coordinates.
"""

from __future__ import annotations

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

try:
    from ...services.mouse_automation import get_mouse_position
    HAVE_MOUSE = True
except:
    HAVE_MOUSE = False


class PositionRecorder(QWidget):
    """Widget for recording mouse positions."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.recorded_positions = []
        self._setup_ui()
        self._start_position_tracking()

    def _setup_ui(self) -> None:
        """Setup the UI."""
        self.setWindowTitle("🎯 Position Recorder")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Title
        title = QLabel("🎯 Mouse Position Recorder")
        title.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(title)
        
        # Instructions
        instructions = QLabel(
            "Move your mouse to the position you want to click,\n"
            "then press 'Record Position'.\n\n"
            "Example: Hover over your mic button, then record."
        )
        instructions.setStyleSheet("color: #888; font-size: 11px;")
        instructions.setWordWrap(True)
        layout.addWidget(instructions)
        
        # Current position display
        position_group = QGroupBox("Current Mouse Position")
        position_layout = QVBoxLayout()
        
        self.position_label = QLabel("X: 0, Y: 0")
        self.position_label.setStyleSheet(
            "font-size: 16px; font-weight: bold; "
            "color: #00ff00; background: #1a1a1a; "
            "padding: 10px; border-radius: 5px;"
        )
        self.position_label.setAlignment(Qt.AlignCenter)
        position_layout.addWidget(self.position_label)
        
        position_group.setLayout(position_layout)
        layout.addWidget(position_group)
        
        # Record button
        self.record_btn = QPushButton("📍 Record This Position")
        self.record_btn.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 12px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        self.record_btn.clicked.connect(self._record_position)
        layout.addWidget(self.record_btn)
        
        # Recorded positions
        recorded_group = QGroupBox("Recorded Positions")
        recorded_layout = QVBoxLayout()
        
        self.recorded_label = QLabel("No positions recorded yet")
        self.recorded_label.setStyleSheet("color: #888; font-size: 11px;")
        self.recorded_label.setWordWrap(True)
        recorded_layout.addWidget(self.recorded_label)
        
        # Copy button
        self.copy_btn = QPushButton("📋 Copy Last Position")
        self.copy_btn.setEnabled(False)
        self.copy_btn.clicked.connect(self._copy_last_position)
        recorded_layout.addWidget(self.copy_btn)
        
        # Test button
        self.test_btn = QPushButton("🖱️ Test Last Position")
        self.test_btn.setEnabled(False)
        self.test_btn.clicked.connect(self._test_last_position)
        recorded_layout.addWidget(self.test_btn)
        
        recorded_group.setLayout(recorded_layout)
        layout.addWidget(recorded_group)
        
        # Quick actions
        actions_layout = QHBoxLayout()
        
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.clicked.connect(self._clear_positions)
        actions_layout.addWidget(clear_btn)
        
        close_btn = QPushButton("✖ Close")
        close_btn.clicked.connect(self.hide)
        actions_layout.addWidget(close_btn)
        
        layout.addLayout(actions_layout)
        
        self.setFixedWidth(350)

    def _start_position_tracking(self) -> None:
        """Start tracking mouse position."""
        if not HAVE_MOUSE:
            self.position_label.setText("Mouse tracking unavailable")
            return
        
        self.position_timer = QTimer(self)
        self.position_timer.timeout.connect(self._update_position)
        self.position_timer.start(50)  # Update every 50ms

    def _update_position(self) -> None:
        """Update current position display."""
        if not HAVE_MOUSE:
            return
        
        x, y = get_mouse_position()
        self.position_label.setText(f"X: {x}, Y: {y}")

    def _record_position(self) -> None:
        """Record current mouse position."""
        if not HAVE_MOUSE:
            return
        
        x, y = get_mouse_position()
        self.recorded_positions.append((x, y))
        
        # Update display
        positions_text = "\n".join([
            f"{i+1}. X: {pos[0]}, Y: {pos[1]}" 
            for i, pos in enumerate(self.recorded_positions)
        ])
        self.recorded_label.setText(positions_text)
        
        # Enable buttons
        self.copy_btn.setEnabled(True)
        self.test_btn.setEnabled(True)
        
        print(f"📍 Recorded position: ({x}, {y})")

    def _copy_last_position(self) -> None:
        """Copy last recorded position to clipboard."""
        if not self.recorded_positions:
            return
        
        import pyperclip
        x, y = self.recorded_positions[-1]
        text = f"{x}, {y}"
        pyperclip.copy(text)
        
        self.recorded_label.setText(
            self.recorded_label.text() + 
            f"\n\n✅ Copied to clipboard: {text}"
        )
        print(f"📋 Copied position: {text}")

    def _test_last_position(self) -> None:
        """Test click at last recorded position."""
        if not self.recorded_positions:
            return
        
        from ...services.mouse_automation import quick_click
        
        x, y = self.recorded_positions[-1]
        
        # Give user time to see the click
        self.test_btn.setText("🖱️ Clicking in 2 seconds...")
        self.test_btn.setEnabled(False)
        
        QTimer.singleShot(2000, lambda: self._do_test_click(x, y))

    def _do_test_click(self, x: int, y: int) -> None:
        """Perform the test click."""
        from ...services.mouse_automation import quick_click
        
        success = quick_click(x, y)
        
        if success:
            self.recorded_label.setText(
                self.recorded_label.text() + 
                f"\n\n✅ Test click successful at ({x}, {y})"
            )
        else:
            self.recorded_label.setText(
                self.recorded_label.text() + 
                f"\n\n❌ Test click failed"
            )
        
        self.test_btn.setText("🖱️ Test Last Position")
        self.test_btn.setEnabled(True)

    def _clear_positions(self) -> None:
        """Clear all recorded positions."""
        self.recorded_positions.clear()
        self.recorded_label.setText("No positions recorded yet")
        self.copy_btn.setEnabled(False)
        self.test_btn.setEnabled(False)
        print("🗑️ Cleared all positions")
