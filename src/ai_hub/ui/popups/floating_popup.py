"""Floating popup window for WritingTools-style UI - shows results in a temporary window."""

from __future__ import annotations

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QFont, QClipboard
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QApplication,
)


class FloatingPopup(QWidget):
    """Floating popup window for displaying AI results (WritingTools style)."""

    def __init__(
        self,
        title: str = "AI Hub",
        original_text: str = "",
        result_text: str = "",
        on_copy=None,
        on_apply=None,
        parent=None,
    ):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self._on_copy = on_copy
        self._on_apply = on_apply
        self._result_text = result_text
        self._original_text = original_text

        self._setup_ui()
        self._apply_theme()
        self._position_window()
        self.resize(600, 400)

    def _setup_ui(self) -> None:
        """Setup the UI layout."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        # Title
        title_label = QLabel(self.windowTitle())
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # Result display
        self._result_text_edit = QTextEdit()
        self._result_text_edit.setReadOnly(True)
        self._result_text_edit.setText(self._result_text)
        self._result_text_edit.setMaximumHeight(250)
        layout.addWidget(self._result_text_edit)

        # Original text (if provided)
        if self._original_text:
            original_label = QLabel("Original:")
            original_label.setFont(QFont("Monospace", 8))
            layout.addWidget(original_label)

            self._original_text_edit = QTextEdit()
            self._original_text_edit.setReadOnly(True)
            self._original_text_edit.setText(self._original_text)
            self._original_text_edit.setMaximumHeight(80)
            layout.addWidget(self._original_text_edit)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        copy_btn = QPushButton("Copy")
        copy_btn.clicked.connect(self._on_copy_clicked)
        button_layout.addWidget(copy_btn)

        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self._on_apply_clicked)
        button_layout.addWidget(apply_btn)

        dismiss_btn = QPushButton("Dismiss")
        dismiss_btn.clicked.connect(self.close)
        button_layout.addWidget(dismiss_btn)

        layout.addLayout(button_layout)

    def _apply_theme(self) -> None:
        """Apply dark theme."""
        stylesheet = """
            FloatingPopup {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #404040;
                border-radius: 8px;
            }
            QLabel {
                color: #e0e0e0;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 5px;
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
            cursor_pos = QApplication.instance().screenAt(
                QApplication.instance().cursor().pos()
            ).geometry().center()

        # Offset from cursor
        offset = QPoint(50, 50)
        self.move(cursor_pos + offset)

    def _on_copy_clicked(self) -> None:
        """Copy result to clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self._result_text, QClipboard.Mode.Clipboard)
        if self._on_copy:
            self._on_copy()

    def _on_apply_clicked(self) -> None:
        """Apply result (copy and close)."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self._result_text, QClipboard.Mode.Clipboard)
        if self._on_apply:
            self._on_apply()
        self.close()

    def keyPressEvent(self, event) -> None:
        """Handle Escape key to close."""
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

