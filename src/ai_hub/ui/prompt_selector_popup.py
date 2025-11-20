"""Prompt Selector Popup - Opens with Ctrl+Alt+T to select prompts."""

from __future__ import annotations

import os
import json
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QMessageBox,
    QDialog,
    QApplication,
)


class NewPromptDialog(QDialog):
    """Dialog to create a new prompt."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Prompt")
        self.setGeometry(200, 200, 600, 500)
        self.result_data = None

        self._setup_ui()
        self._apply_theme()

    def _setup_ui(self) -> None:
        """Setup UI."""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Name
        layout.addWidget(QLabel("Prompt Name:", font=QFont("Arial", 10, QFont.Weight.Bold)))
        self._name_input = QLineEdit()
        self._name_input.setPlaceholderText("e.g., Simplify, Professional, etc.")
        self._name_input.setMinimumHeight(35)
        layout.addWidget(self._name_input)

        # Description
        layout.addWidget(QLabel("Description:", font=QFont("Arial", 10, QFont.Weight.Bold)))
        self._desc_input = QLineEdit()
        self._desc_input.setPlaceholderText("Short description shown in popup")
        self._desc_input.setMinimumHeight(35)
        layout.addWidget(self._desc_input)

        # Prompt
        layout.addWidget(QLabel("Prompt Text:", font=QFont("Arial", 10, QFont.Weight.Bold)))
        self._prompt_input = QTextEdit()
        self._prompt_input.setPlaceholderText("The full prompt to send to AI")
        self._prompt_input.setMinimumHeight(150)
        layout.addWidget(self._prompt_input)

        # Testing
        layout.addWidget(QLabel("Testing Notes:", font=QFont("Arial", 10, QFont.Weight.Bold)))
        self._testing_input = QTextEdit()
        self._testing_input.setPlaceholderText("How to test this prompt (optional)")
        self._testing_input.setMinimumHeight(100)
        layout.addWidget(self._testing_input)

        # Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.setMinimumHeight(40)
        save_btn.clicked.connect(self._on_save)
        btn_layout.addWidget(save_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumHeight(40)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_btn)

        layout.addLayout(btn_layout)

    def _on_save(self) -> None:
        """Save new prompt."""
        name = self._name_input.text().strip()
        desc = self._desc_input.text().strip()
        prompt = self._prompt_input.toPlainText().strip()
        testing = self._testing_input.toPlainText().strip()

        if not name or not prompt:
            QMessageBox.warning(self, "Error", "Name and Prompt are required!")
            return

        self.result_data = {
            "name": name,
            "description": desc,
            "prompt": prompt,
            "testing": testing,
        }
        self.accept()

    def _apply_theme(self) -> None:
        """Apply dark theme."""
        stylesheet = """
            QDialog {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QLabel {
                color: #e0e0e0;
            }
            QLineEdit, QTextEdit {
                background-color: #252525;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                padding: 5px;
                border-radius: 3px;
            }
            QLineEdit:focus, QTextEdit:focus {
                border: 1px solid #007acc;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """
        self.setStyleSheet(stylesheet)


class PromptSelectorPopup(QWidget):
    """Popup to select and manage prompts (opens with Ctrl+Alt+T)."""

    def __init__(self, on_select=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Prompt")
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self._on_select = on_select
        self._prompts = []
        self._prompt_file = self._get_prompt_file()

        self._setup_ui()
        self._apply_theme()
        self._load_prompts()
        self._populate_list()
        self._position_window()
        self.resize(500, 600)

    def _get_prompt_file(self) -> str:
        """Get prompt storage file path."""
        config_dir = os.path.join(
            os.path.dirname(__file__), "..", "..", "config"
        )
        os.makedirs(config_dir, exist_ok=True)
        return os.path.join(config_dir, "prompts.json")

    def _setup_ui(self) -> None:
        """Setup UI."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        # Title
        title = QLabel("Select Prompt:")
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(title)

        # Prompt list
        self._list_widget = QListWidget()
        self._list_widget.itemDoubleClicked.connect(self._on_item_selected)
        self._list_widget.itemClicked.connect(self._on_item_clicked)
        layout.addWidget(self._list_widget)

        # Description display
        self._description_label = QLabel()
        self._description_label.setWordWrap(True)
        self._description_label.setStyleSheet("color: #999999; font-size: 10pt; background-color: #2d2d2d; padding: 8px; border-radius: 3px;")
        layout.addWidget(self._description_label)

        # Buttons
        btn_layout = QHBoxLayout()

        use_btn = QPushButton("Use This Prompt")
        use_btn.setMinimumHeight(35)
        use_btn.clicked.connect(self._on_item_selected)
        btn_layout.addWidget(use_btn)

        new_btn = QPushButton("New Prompt")
        new_btn.setMinimumHeight(35)
        new_btn.clicked.connect(self._on_new_prompt)
        btn_layout.addWidget(new_btn)

        delete_btn = QPushButton("Delete")
        delete_btn.setMinimumHeight(35)
        delete_btn.clicked.connect(self._on_delete)
        btn_layout.addWidget(delete_btn)

        close_btn = QPushButton("Close")
        close_btn.setMinimumHeight(35)
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)

        layout.addLayout(btn_layout)

    def _on_item_clicked(self) -> None:
        """Show description when item clicked."""
        current_item = self._list_widget.currentItem()
        if current_item:
            idx = current_item.data(Qt.ItemDataRole.UserRole)
            if 0 <= idx < len(self._prompts):
                prompt = self._prompts[idx]
                desc = prompt.get("description", "")
                if desc:
                    self._description_label.setText(f"📝 {desc}")
                else:
                    self._description_label.setText("(No description)")

    def _on_item_selected(self) -> None:
        """Use selected prompt."""
        current_item = self._list_widget.currentItem()
        if current_item:
            idx = current_item.data(Qt.ItemDataRole.UserRole)
            if 0 <= idx < len(self._prompts):
                prompt = self._prompts[idx]
                if self._on_select:
                    self._on_select(prompt)
                self.close()

    def _on_new_prompt(self) -> None:
        """Create new prompt."""
        dialog = NewPromptDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            if dialog.result_data:
                self._prompts.append(dialog.result_data)
                self._save_prompts()
                self._populate_list()
                QMessageBox.information(self, "Success", "Prompt saved!")

    def _on_delete(self) -> None:
        """Delete selected prompt."""
        current_item = self._list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Error", "Select a prompt to delete!")
            return

        idx = current_item.data(Qt.ItemDataRole.UserRole)
        if 0 <= idx < len(self._prompts):
            if QMessageBox.question(
                self,
                "Confirm",
                "Delete this prompt?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            ) == QMessageBox.StandardButton.Yes:
                self._prompts.pop(idx)
                self._save_prompts()
                self._populate_list()

    def _populate_list(self) -> None:
        """Populate list widget."""
        self._list_widget.clear()
        for i, prompt in enumerate(self._prompts):
            name = prompt.get("name", f"Prompt {i+1}")
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, i)
            self._list_widget.addItem(item)

    def _save_prompts(self) -> None:
        """Save prompts to file."""
        with open(self._prompt_file, "w") as f:
            json.dump(self._prompts, f, indent=2)

    def _load_prompts(self) -> None:
        """Load prompts from file."""
        if os.path.exists(self._prompt_file):
            try:
                with open(self._prompt_file, "r") as f:
                    data = json.load(f)
                    self._prompts = data if isinstance(data, list) else []
            except Exception as e:
                print(f"Error loading prompts: {e}")

        # If no prompts, add defaults
        if not self._prompts:
            self._prompts = [
                {
                    "name": "Simplify",
                    "description": "Make text simpler and easier to understand",
                    "prompt": "Simplify this text while keeping the same meaning. Use simple words and short sentences.",
                },
                {
                    "name": "Professional",
                    "description": "Use formal, professional tone",
                    "prompt": "Rewrite this text in a formal, professional tone suitable for business.",
                },
                {
                    "name": "Friendly",
                    "description": "Use casual, friendly tone",
                    "prompt": "Rewrite this text in a casual, friendly tone. Be warm and approachable.",
                },
                {
                    "name": "Expand",
                    "description": "Add more detail and examples",
                    "prompt": "Expand this text with more details, examples, and explanations.",
                },
            ]
            self._save_prompts()

    def _position_window(self) -> None:
        """Position window near cursor."""
        try:
            cursor_pos = QApplication.instance().inputMethod().cursorRectangle().topLeft()
            if cursor_pos.isNull():
                screen = QApplication.instance().screenAt(QApplication.instance().cursor().pos())
                cursor_pos = screen.geometry().center()

            offset = QPoint(50, 50)
            self.move(cursor_pos + offset)
        except Exception:
            # Fallback to center screen
            pass

    def _apply_theme(self) -> None:
        """Apply dark theme."""
        stylesheet = """
            PromptSelectorPopup {
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
                padding: 6px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """
        self.setStyleSheet(stylesheet)

    def keyPressEvent(self, event) -> None:
        """Handle Escape key."""
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)


