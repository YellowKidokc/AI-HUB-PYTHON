"""Prompt selector popup - choose from custom prompts."""

from __future__ import annotations

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QApplication,
)


class PromptSelector(QWidget):
    """Popup to select from custom prompts."""

    def __init__(self, prompts: list[dict], on_select=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AI Hub - Choose Prompt")
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self._prompts = prompts
        self._on_select = on_select
        self._selected_prompt = None

        self._setup_ui()
        self._apply_theme()
        self._position_window()
        self.resize(400, 350)

    def _setup_ui(self) -> None:
        """Setup UI layout."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        # Title
        title = QLabel("Select a Prompt:")
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        # Prompt list
        self._list_widget = QListWidget()
        self._list_widget.itemDoubleClicked.connect(self._on_item_selected)
        for i, prompt in enumerate(self._prompts):
            item = QListWidgetItem(prompt.get("name", f"Prompt {i+1}"))
            item.setData(Qt.ItemDataRole.UserRole, i)
            self._list_widget.addItem(item)
        layout.addWidget(self._list_widget)

        # Description
        self._description = QLabel()
        self._description.setWordWrap(True)
        self._description.setStyleSheet("color: #999999; font-size: 9pt;")
        layout.addWidget(self._description)

        # Connect selection change to show description
        self._list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        select_btn = QPushButton("Select")
        select_btn.clicked.connect(self._on_item_selected)
        button_layout.addWidget(select_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

    def _on_selection_changed(self) -> None:
        """Update description when selection changes."""
        current_item = self._list_widget.currentItem()
        if current_item:
            idx = current_item.data(Qt.ItemDataRole.UserRole)
            prompt = self._prompts[idx]
            self._description.setText(prompt.get("description", ""))

    def _on_item_selected(self) -> None:
        """Handle item selection."""
        current_item = self._list_widget.currentItem()
        if current_item:
            idx = current_item.data(Qt.ItemDataRole.UserRole)
            self._selected_prompt = self._prompts[idx]
            if self._on_select:
                self._on_select(self._selected_prompt)
            self.close()

    def _apply_theme(self) -> None:
        """Apply dark theme."""
        stylesheet = """
            PromptSelector {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #404040;
                border-radius: 8px;
            }
            QLabel {
                color: #e0e0e0;
            }
            QListWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #007acc;
            }
            QListWidget::item:hover {
                background-color: #404040;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                padding: 6px 16px;
                border-radius: 4px;
                font-weight: bold;
                min-width: 70px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
        """
        self.setStyleSheet(stylesheet)

    def _position_window(self) -> None:
        """Position window near cursor."""
        cursor_pos = QApplication.instance().inputMethod().cursorRectangle().topLeft()
        if cursor_pos.isNull():
            screen = QApplication.instance().screenAt(
                QApplication.instance().cursor().pos()
            )
            cursor_pos = screen.geometry().center()

        offset = QPoint(50, 50)
        self.move(cursor_pos + offset)

    def keyPressEvent(self, event) -> None:
        """Handle Escape key."""
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

