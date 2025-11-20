"""
Floating Audio Player Widget

A small, draggable window with play/pause/stop controls for TTS playback.
"""

from __future__ import annotations

from PySide6.QtCore import QPoint, Qt, QTimer
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ...services.window_manager import get_window_settings


class FloatingPlayer(QWidget):
    """Small draggable audio player with controls."""

    def __init__(self, audio_engine, window_control_panel=None):
        super().__init__()
        self.audio_engine = audio_engine
        self.window_control_panel = window_control_panel
        self.window_settings = get_window_settings()
        self._dragging = False
        self._drag_position = QPoint()
        self._is_paused = False
        
        self._setup_ui()
        self._setup_timer()
        self._load_saved_position()

    def _setup_ui(self) -> None:
        """Setup the UI."""
        # Window flags for floating behavior
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool
        )
        
        # Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                border: 2px solid #007acc;
                border-radius: 8px;
            }
            QPushButton {
                background-color: #404040;
                color: white;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 8px;
                font-size: 16px;
                min-width: 40px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #505050;
                border: 1px solid #007acc;
            }
            QPushButton:pressed {
                background-color: #007acc;
            }
            QLabel {
                color: white;
                font-size: 11px;
                padding: 2px;
            }
        """)
        
        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(4)
        
        # Title bar (for dragging)
        title_layout = QHBoxLayout()
        self.title_label = QLabel("🎙️ TTS Player")
        self.title_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        title_layout.addWidget(self.title_label)
        
        self.close_btn = QPushButton("×")
        self.close_btn.setMaximumWidth(30)
        self.close_btn.setMaximumHeight(25)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #d32f2f;
                min-width: 25px;
                min-height: 25px;
                padding: 2px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f44336;
            }
        """)
        self.close_btn.clicked.connect(self.hide)
        title_layout.addWidget(self.close_btn)
        main_layout.addLayout(title_layout)
        
        # Status label
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #888; font-style: italic;")
        main_layout.addWidget(self.status_label)
        
        # Control buttons
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(6)
        
        self.play_pause_btn = QPushButton("▶️")
        self.play_pause_btn.setToolTip("Play/Pause")
        self.play_pause_btn.clicked.connect(self._toggle_play_pause)
        
        self.stop_btn = QPushButton("⏹️")
        self.stop_btn.setToolTip("Stop")
        self.stop_btn.clicked.connect(self._stop)
        
        controls_layout.addWidget(self.play_pause_btn)
        controls_layout.addWidget(self.stop_btn)
        
        main_layout.addLayout(controls_layout)
        
        # Window Manager button
        if self.window_control_panel:
            manager_btn = QPushButton("🎮")
            manager_btn.setToolTip("Window Manager")
            manager_btn.setMaximumWidth(40)
            manager_btn.clicked.connect(self._show_window_manager)
            main_layout.addWidget(manager_btn)
        
        # Set size
        self.setFixedSize(200, 140)
        
        # Position will be loaded from settings or default to bottom-right

    def _setup_timer(self) -> None:
        """Setup timer to update status."""
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self._update_status)
        self.update_timer.start(100)  # Update every 100ms

    def _position_bottom_right(self) -> None:
        """Position window in bottom-right corner of screen."""
        screen = self.screen().geometry()
        x = screen.width() - self.width() - 20
        y = screen.height() - self.height() - 60
        self.move(x, y)

    def _load_saved_position(self) -> None:
        """Load saved position from settings."""
        settings = self.window_settings.get_window_settings("floating_player")
        
        if settings:
            x = settings.get("x", -1)
            y = settings.get("y", -1)
            
            if x >= 0 and y >= 0:
                self.move(x, y)
                print(f"✅ Loaded floating player position: {x},{y}")
                return
        
        # Default to bottom-right if no saved position
        self._position_bottom_right()

    def _show_window_manager(self) -> None:
        """Show the window manager panel."""
        if self.window_control_panel:
            self.window_control_panel.show()
            self.window_control_panel.raise_()
            self.window_control_panel.activateWindow()

    def _toggle_play_pause(self) -> None:
        """Toggle between play and pause."""
        if not self.audio_engine:
            self.status_label.setText("Engine not ready")
            return
        
        # Check if currently playing
        is_playing = self.audio_engine.is_playing()
        
        if is_playing:
            if self._is_paused:
                # Resume playback
                if self.audio_engine.resume_playback():
                    self.play_pause_btn.setText("⏸️")
                    self._is_paused = False
                    self.status_label.setText("🔊 Playing...")
                    print("▶️ Resumed playback")
            else:
                # Pause playback
                if self.audio_engine.pause_playback():
                    self.play_pause_btn.setText("▶️")
                    self._is_paused = True
                    self.status_label.setText("⏸️ Paused")
                    print("⏸️ Paused playback")
        else:
            # Not playing - try to resume if paused
            if self._is_paused:
                if self.audio_engine.resume_playback():
                    self.play_pause_btn.setText("⏸️")
                    self._is_paused = False
                    self.status_label.setText("🔊 Playing...")
                    print("▶️ Resumed playback")
            else:
                self.status_label.setText("No audio to play")
                print("⚠️ No audio currently loaded")

    def _stop(self) -> None:
        """Stop playback."""
        if not self.audio_engine:
            return
        
        self.audio_engine.stop_playback()
        self.play_pause_btn.setText("▶️")
        self._is_paused = False
        self.status_label.setText("Stopped")

    def _update_status(self) -> None:
        """Update status label based on playback state."""
        if not self.audio_engine:
            return
        
        if self.audio_engine.is_playing():
            if not self._is_paused:
                self.status_label.setText("🔊 Playing...")
                self.play_pause_btn.setText("⏸️")
        else:
            if self.status_label.text() == "🔊 Playing...":
                self.status_label.setText("✅ Finished")
                self.play_pause_btn.setText("▶️")
                self._is_paused = False

    def set_speaking(self, text: str) -> None:
        """Called when TTS starts speaking."""
        self.status_label.setText("🔊 Speaking...")
        self.play_pause_btn.setText("⏸️")
        self._is_paused = False
        self.show()
        self.raise_()

    # --- Dragging functionality ---
    
    def mousePressEvent(self, event) -> None:
        """Handle mouse press for dragging."""
        if event.button() == Qt.LeftButton:
            # Only allow dragging from title area
            if event.position().y() < 30:
                self._dragging = True
                self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                event.accept()

    def mouseMoveEvent(self, event) -> None:
        """Handle mouse move for dragging."""
        if self._dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event) -> None:
        """Handle mouse release."""
        if event.button() == Qt.LeftButton:
            self._dragging = False
            event.accept()
