from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from ...services.openai_client import OpenAIClient
from ...services.prompt_manager import Prompt
from ..tabs.base import BaseTab


class ShortcutsManagerTab(BaseTab):
    """AHK-style shortcuts manager with visual editor."""

    def __init__(self, client: OpenAIClient, prompts: list[Prompt]):
        super().__init__()
        self._client = client
        self._prompts = prompts
        self.shortcuts: list[dict[str, Any]] = []
        self.shortcuts_file = Path("config/shortcuts.json")
        self.load_shortcuts()
        self._build_ui()

    def _build_ui(self) -> None:
        main_layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)

        # --- LEFT COLUMN (EDITOR) ---
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        editor_layout.setContentsMargins(0, 0, 10, 0)

        # Title
        title_label = QLabel("<h2>Shortcut Editor</h2>")
        editor_layout.addWidget(title_label)

        # Type Selection
        editor_layout.addWidget(QLabel("<b>Type:</b>"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Hotkey", "Hotstring"])
        self.type_combo.currentTextChanged.connect(self.toggle_inputs)
        editor_layout.addWidget(self.type_combo)

        # Action Selection
        editor_layout.addWidget(QLabel("<b>Action:</b>"))
        self.action_combo = QComboBox()
        self.action_combo.addItems(["Send Text", "Run Program", "AI Rewrite", "Mouse Click"])
        self.action_combo.currentTextChanged.connect(self._on_action_changed)
        editor_layout.addWidget(self.action_combo)

        # Modifiers Group (Ctrl, Alt, etc.)
        self.mod_group = QGroupBox("Modifiers (For Hotkeys)")
        mod_layout = QHBoxLayout()
        self.chk_ctrl = QCheckBox("Ctrl")
        self.chk_alt = QCheckBox("Alt")
        self.chk_shift = QCheckBox("Shift")
        self.chk_win = QCheckBox("Win")
        mod_layout.addWidget(self.chk_ctrl)
        mod_layout.addWidget(self.chk_alt)
        mod_layout.addWidget(self.chk_shift)
        mod_layout.addWidget(self.chk_win)
        self.mod_group.setLayout(mod_layout)
        editor_layout.addWidget(self.mod_group)

        # Trigger Key / Abbreviation
        self.lbl_trigger = QLabel("<b>Key (e.g., 'space') or Trigger String:</b>")
        editor_layout.addWidget(self.lbl_trigger)
        self.txt_trigger = QLineEdit()
        self.txt_trigger.setPlaceholderText("e.g., 'k' or 'btw'")
        editor_layout.addWidget(self.txt_trigger)

        # Description
        editor_layout.addWidget(QLabel("<b>Description:</b>"))
        self.txt_desc = QLineEdit()
        self.txt_desc.setPlaceholderText("Brief description of what this does")
        editor_layout.addWidget(self.txt_desc)

        # Output / Payload
        self.lbl_output = QLabel("<b>Output Text / AI Prompt / Path:</b>")
        editor_layout.addWidget(self.lbl_output)
        self.txt_output = QPlainTextEdit()
        self.txt_output.setMaximumHeight(150)
        self.txt_output.setPlaceholderText(
            "For 'Send Text': Type the text to send\n"
            "For 'Run Program': Enter the program path\n"
            "For 'AI Rewrite': Enter the AI instruction\n"
            "For 'Mouse Click': Enter X, Y coordinates (e.g., '100, 200')"
        )
        editor_layout.addWidget(self.txt_output)
        
        # Mouse Click specific fields (hidden by default)
        self.mouse_group = QGroupBox("🖱️ Mouse Click Settings")
        mouse_layout = QVBoxLayout()
        
        # Position recorder button
        record_btn = QPushButton("🎯 Open Position Recorder")
        record_btn.setToolTip("Record mouse positions for automation")
        record_btn.clicked.connect(self._open_position_recorder)
        mouse_layout.addWidget(record_btn)
        
        # Click count
        click_layout = QHBoxLayout()
        click_layout.addWidget(QLabel("Clicks:"))
        self.click_count = QComboBox()
        self.click_count.addItems(["1 (Single)", "2 (Double)", "3 (Triple)"])
        click_layout.addWidget(self.click_count)
        click_layout.addStretch()
        mouse_layout.addLayout(click_layout)
        
        # Info
        mouse_info = QLabel(
            "💡 Tip: Use Position Recorder to find exact coordinates.\n"
            "Perfect for toggling mic, clicking buttons, etc."
        )
        mouse_info.setStyleSheet("color: #888; font-size: 10px; font-style: italic;")
        mouse_info.setWordWrap(True)
        mouse_layout.addWidget(mouse_info)
        
        self.mouse_group.setLayout(mouse_layout)
        self.mouse_group.setVisible(False)  # Hidden by default
        editor_layout.addWidget(self.mouse_group)

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_save = QPushButton("💾 Add / Save")
        self.btn_save.setStyleSheet(
            "background-color: #007acc; color: white; font-weight: bold; padding: 8px;"
        )
        self.btn_save.clicked.connect(self.save_shortcut)

        self.btn_clear = QPushButton("🗑️ Clear Form")
        self.btn_clear.clicked.connect(self.clear_form)

        self.btn_delete = QPushButton("❌ Delete Selected")
        self.btn_delete.clicked.connect(self.delete_shortcut)

        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_clear)
        btn_layout.addWidget(self.btn_delete)
        editor_layout.addLayout(btn_layout)
        editor_layout.addStretch()

        # --- RIGHT COLUMN (LIBRARY) ---
        library_widget = QWidget()
        library_layout = QVBoxLayout(library_widget)
        library_layout.setContentsMargins(10, 0, 0, 0)

        library_layout.addWidget(QLabel("<h2>📚 Shortcuts Library</h2>"))
        
        # Info label
        info_label = QLabel("Click a row to edit. Changes take effect after restart.")
        info_label.setStyleSheet("color: #888; font-style: italic;")
        library_layout.addWidget(info_label)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Type", "Trigger", "Description", "Output Preview"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.itemClicked.connect(self.load_from_table)
        library_layout.addWidget(self.table)

        # Add widgets to splitter
        splitter.addWidget(editor_widget)
        splitter.addWidget(library_widget)
        splitter.setStretchFactor(0, 1)  # Editor
        splitter.setStretchFactor(1, 2)  # Library takes more space

        main_layout.addWidget(splitter)
        self.refresh_table()

    def toggle_inputs(self, text: str) -> None:
        """Hide modifiers if Hotstring is selected."""
        is_hotkey = text == "Hotkey"
        self.mod_group.setVisible(is_hotkey)
        if is_hotkey:
            self.lbl_trigger.setText("<b>Key (e.g., 'space', 'k', 'f1'):</b>")
            self.txt_trigger.setPlaceholderText("e.g., 'space', 'k', 'f1'")
        else:
            self.lbl_trigger.setText("<b>Abbreviation (e.g., 'btw', 'addr'):</b>")
            self.txt_trigger.setPlaceholderText("e.g., 'btw', 'addr', 'sig'")

    def save_shortcut(self) -> None:
        """Save the current shortcut to the list."""
        # Gather Data
        entry = {
            "type": self.type_combo.currentText(),
            "action": self.action_combo.currentText(),
            "trigger": self.txt_trigger.text().strip(),
            "desc": self.txt_desc.text().strip(),
            "output": self.txt_output.toPlainText().strip(),
            "modifiers": [],
        }

        if entry["type"] == "Hotkey":
            if self.chk_ctrl.isChecked():
                entry["modifiers"].append("ctrl")
            if self.chk_alt.isChecked():
                entry["modifiers"].append("alt")
            if self.chk_shift.isChecked():
                entry["modifiers"].append("shift")
            if self.chk_win.isChecked():
                entry["modifiers"].append("windows")

        # Basic Validation
        if not entry["trigger"]:
            QMessageBox.warning(self, "Error", "⚠️ Trigger is required!")
            return

        if not entry["output"]:
            QMessageBox.warning(self, "Error", "⚠️ Output/Action content is required!")
            return

        # Save to list
        self.shortcuts.append(entry)
        self.save_to_disk()
        self.refresh_table()

        # Clear inputs
        self.clear_form()
        
        QMessageBox.information(
            self,
            "Success",
            "✅ Shortcut saved!\n\nRestart the app for changes to take effect.",
        )

    def clear_form(self) -> None:
        """Clear all input fields."""
        self.txt_trigger.clear()
        self.txt_desc.clear()
        self.txt_output.clear()
        self.chk_ctrl.setChecked(False)
        self.chk_alt.setChecked(False)
        self.chk_shift.setChecked(False)
        self.chk_win.setChecked(False)

    def delete_shortcut(self) -> None:
        """Delete the selected shortcut."""
        row = self.table.currentRow()
        if row >= 0:
            reply = QMessageBox.question(
                self,
                "Confirm Delete",
                f"Delete shortcut: {self.shortcuts[row]['desc']}?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                del self.shortcuts[row]
                self.save_to_disk()
                self.refresh_table()
                self.clear_form()
                QMessageBox.information(
                    self, "Deleted", "✅ Shortcut deleted. Restart to apply changes."
                )

    def load_from_table(self, item: QTableWidgetItem) -> None:
        """Load a shortcut from the table into the editor."""
        row = item.row()
        if row < 0 or row >= len(self.shortcuts):
            return

        data = self.shortcuts[row]

        self.type_combo.setCurrentText(data["type"])
        self.action_combo.setCurrentText(data["action"])
        self.txt_trigger.setText(data["trigger"])
        self.txt_desc.setText(data["desc"])
        self.txt_output.setPlainText(data["output"])

        # Reset checks
        self.chk_ctrl.setChecked(False)
        self.chk_alt.setChecked(False)
        self.chk_shift.setChecked(False)
        self.chk_win.setChecked(False)

        if "modifiers" in data:
            if "ctrl" in data["modifiers"]:
                self.chk_ctrl.setChecked(True)
            if "alt" in data["modifiers"]:
                self.chk_alt.setChecked(True)
            if "shift" in data["modifiers"]:
                self.chk_shift.setChecked(True)
            if "windows" in data["modifiers"]:
                self.chk_win.setChecked(True)

    def _on_action_changed(self, action: str) -> None:
        """Handle action type change."""
        # Show/hide mouse group based on action
        is_mouse_click = action == "Mouse Click"
        self.mouse_group.setVisible(is_mouse_click)
        
        # Update label text
        if is_mouse_click:
            self.lbl_output.setText("<b>Mouse Position (X, Y):</b>")
        else:
            self.lbl_output.setText("<b>Output Text / AI Prompt / Path:</b>")

    def _open_position_recorder(self) -> None:
        """Open the position recorder tool."""
        from ..widgets.position_recorder import PositionRecorder
        
        if not hasattr(self, 'position_recorder'):
            self.position_recorder = PositionRecorder()
        
        self.position_recorder.show()
        self.position_recorder.raise_()
        self.position_recorder.activateWindow()

    def refresh_table(self) -> None:
        """Refresh the shortcuts table."""
        self.table.setRowCount(len(self.shortcuts))
        for i, s in enumerate(self.shortcuts):
            trig_display = s["trigger"]
            if s["type"] == "Hotkey" and s.get("modifiers"):
                trig_display = "+".join(s["modifiers"]) + "+" + s["trigger"]

            self.table.setItem(i, 0, QTableWidgetItem(s["type"]))
            self.table.setItem(i, 1, QTableWidgetItem(trig_display))
            self.table.setItem(i, 2, QTableWidgetItem(s["desc"]))
            preview = s["output"][:50] + ("..." if len(s["output"]) > 50 else "")
            self.table.setItem(i, 3, QTableWidgetItem(preview))

    def save_to_disk(self) -> None:
        """Save shortcuts to JSON file."""
        self.shortcuts_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.shortcuts_file, "w", encoding="utf-8") as f:
            json.dump(self.shortcuts, f, indent=4, ensure_ascii=False)

    def load_shortcuts(self) -> None:
        """Load shortcuts from JSON file."""
        if self.shortcuts_file.exists():
            try:
                with open(self.shortcuts_file, "r", encoding="utf-8") as f:
                    self.shortcuts = json.load(f)
            except Exception as e:
                print(f"Error loading shortcuts: {e}")
                self.shortcuts = []
        else:
            self.shortcuts = []
