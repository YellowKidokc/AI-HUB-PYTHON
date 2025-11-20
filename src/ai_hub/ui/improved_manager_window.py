"""Improved Hotkeys & Hotstrings Manager with better UI and hotkey display."""

from __future__ import annotations

import os
import json
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QCheckBox,
    QGroupBox,
)


class HotkeyDisplayHelper:
    """Convert hotkey format: ^!L -> CTRL + ALT + L"""

    @staticmethod
    def format_hotkey_for_display(trigger: str) -> str:
        """Convert ^!+# format to readable CTRL + ALT + SHIFT + WIN format."""
        display = ""
        modifiers = []

        # Check each modifier
        if "^" in trigger:
            modifiers.append("CTRL")
            trigger = trigger.replace("^", "")
        if "!" in trigger:
            modifiers.append("ALT")
            trigger = trigger.replace("!", "")
        if "+" in trigger:
            modifiers.append("SHIFT")
            trigger = trigger.replace("+", "")
        if "#" in trigger:
            modifiers.append("WIN")
            trigger = trigger.replace("#", "")
        if "CapsLock" in trigger:
            modifiers.append("CAPSLOCK")
            trigger = trigger.replace("CapsLock & ", "")

        # Build display string
        if modifiers:
            display = " + ".join(modifiers)
            if trigger:
                display += " + " + trigger.upper()
        else:
            display = trigger.upper()

        return display

    @staticmethod
    def parse_display_to_hotkey(ctrl: bool, alt: bool, shift: bool, win: bool, capslock: bool, key: str) -> str:
        """Convert UI checkboxes and key to hotkey format."""
        trigger = ""
        if ctrl:
            trigger += "^"
        if alt:
            trigger += "!"
        if shift:
            trigger += "+"
        if win:
            trigger += "#"
        if capslock:
            trigger += "CapsLock & "
        trigger += key
        return trigger


class ImprovedHotkeysManagerWindow(QMainWindow):
    """Improved manager with better UI, larger checkboxes, readable hotkey display."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Shortcuts & Hotstrings Manager - Improved")
        self.setGeometry(100, 100, 1200, 700)

        self._items = []
        self._editing_index = None
        self._status_timer = None

        self._setup_ui()
        self._apply_theme()
        self._load_all()
        self._populate_table()

    def _setup_ui(self) -> None:
        """Setup main UI."""
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        # Left panel - Editor
        left_panel = self._create_left_panel()
        layout.addWidget(left_panel)

        # Right panel - Library
        right_panel = self._create_right_panel()
        layout.addWidget(right_panel)

        layout.setStretch(0, 0)
        layout.setStretch(1, 1)

    def _create_left_panel(self) -> QWidget:
        """Create left editor panel."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        # Type selector
        layout.addWidget(QLabel("Type:", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._type_combo = QComboBox()
        self._type_combo.addItems(["Hotkey", "Hotstring"])
        self._type_combo.currentTextChanged.connect(self._on_type_changed)
        self._type_combo.setMinimumHeight(35)
        layout.addWidget(self._type_combo)

        # Action type
        layout.addWidget(QLabel("Action (Hotkey):", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._action_combo = QComboBox()
        self._action_combo.addItems(["Send Text", "Run Program/URL"])
        self._action_combo.setMinimumHeight(35)
        layout.addWidget(self._action_combo)

        # Modifiers group - LARGER CHECKBOXES
        layout.addWidget(QLabel("Modifiers (Hotkey):", font=QFont("Arial", 11, QFont.Weight.Bold)))
        
        mod_group = QGroupBox("Select Modifiers")
        mod_layout = QVBoxLayout(mod_group)

        # Make checkboxes much larger
        self._check_ctrl = QCheckBox("CTRL (^)")
        self._check_ctrl.setMinimumHeight(40)
        self._check_ctrl.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        mod_layout.addWidget(self._check_ctrl)

        self._check_alt = QCheckBox("ALT (!)")
        self._check_alt.setMinimumHeight(40)
        self._check_alt.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        mod_layout.addWidget(self._check_alt)

        self._check_shift = QCheckBox("SHIFT (+)")
        self._check_shift.setMinimumHeight(40)
        self._check_shift.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        mod_layout.addWidget(self._check_shift)

        self._check_win = QCheckBox("WIN (#)")
        self._check_win.setMinimumHeight(40)
        self._check_win.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        mod_layout.addWidget(self._check_win)

        self._check_capslock = QCheckBox("CAPSLOCK")
        self._check_capslock.setMinimumHeight(40)
        self._check_capslock.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        mod_layout.addWidget(self._check_capslock)

        layout.addWidget(mod_group)

        # Key input
        layout.addWidget(QLabel("Key (Hotkey):", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._key_input = QLineEdit()
        self._key_input.setPlaceholderText("e.g., J, SPACE, ENTER")
        self._key_input.setMinimumHeight(35)
        layout.addWidget(self._key_input)

        # Display the built hotkey - LARGER FONT
        layout.addWidget(QLabel("Built Hotkey:", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._hotkey_display = QLabel("(Select modifiers and key)")
        self._hotkey_display.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self._hotkey_display.setStyleSheet("color: #007acc; padding: 10px; background-color: #2d2d2d; border-radius: 4px;")
        layout.addWidget(self._hotkey_display)

        # Connect to update display
        for check in [self._check_ctrl, self._check_alt, self._check_shift, self._check_win, self._check_capslock]:
            check.stateChanged.connect(self._update_hotkey_display)
        self._key_input.textChanged.connect(self._update_hotkey_display)

        # Trigger (for hotstrings)
        layout.addWidget(QLabel("Hotstring Trigger (UPPERCASE 1-32):", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._trigger_input = QLineEdit()
        self._trigger_input.setPlaceholderText("e.g., LOW, EMAIL, SIG")
        self._trigger_input.setMinimumHeight(35)
        layout.addWidget(self._trigger_input)

        # Description
        layout.addWidget(QLabel("Description:", font=QFont("Arial", 11, QFont.Weight.Bold)))
        self._desc_input = QLineEdit()
        self._desc_input.setMinimumHeight(35)
        layout.addWidget(self._desc_input)

        # Output
        layout.addWidget(QLabel("Output / Payload:", font=QFont("Arial", 11, QFont.Weight.Bold)))
        from PySide6.QtWidgets import QTextEdit
        self._output_input = QTextEdit()
        self._output_input.setMinimumHeight(120)
        layout.addWidget(self._output_input)

        # Buttons
        btn_layout = QHBoxLayout()
        self._btn_save = QPushButton("Add/Save")
        self._btn_save.setMinimumHeight(40)
        self._btn_save.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self._btn_save.clicked.connect(self._on_add_or_save)
        btn_layout.addWidget(self._btn_save)

        self._btn_delete = QPushButton("Delete")
        self._btn_delete.setMinimumHeight(40)
        self._btn_delete.clicked.connect(self._on_delete)
        btn_layout.addWidget(self._btn_delete)

        layout.addLayout(btn_layout)

        # Status
        self._status_label = QLabel("Ready.")
        self._status_label.setStyleSheet("color: #AAAAAA;")
        layout.addWidget(self._status_label)

        layout.addStretch()

        # Initial state
        self._on_type_changed()

        return panel

    def _create_right_panel(self) -> QWidget:
        """Create right library panel."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(12, 12, 12, 12)

        layout.addWidget(QLabel("Library", font=QFont("Arial", 12, QFont.Weight.Bold)))

        # Table
        self._table = QTableWidget()
        self._table.setColumnCount(4)
        self._table.setHorizontalHeaderLabels(["Type", "Trigger Display", "Description", "Output Preview"])
        self._table.cellClicked.connect(self._on_table_click)
        layout.addWidget(self._table)

        return panel

    def _update_hotkey_display(self) -> None:
        """Update the hotkey display label."""
        key = self._key_input.text().strip()
        if not key:
            self._hotkey_display.setText("(Select a key)")
            return

        helper = HotkeyDisplayHelper()
        trigger = helper.parse_display_to_hotkey(
            self._check_ctrl.isChecked(),
            self._check_alt.isChecked(),
            self._check_shift.isChecked(),
            self._check_win.isChecked(),
            self._check_capslock.isChecked(),
            key
        )

        display = helper.format_hotkey_for_display(trigger)
        self._hotkey_display.setText(display)

    def _on_type_changed(self) -> None:
        """Handle type change."""
        is_hotkey = self._type_combo.currentText() == "Hotkey"

        for widget in [
            self._action_combo,
            self._check_ctrl,
            self._check_alt,
            self._check_shift,
            self._check_win,
            self._check_capslock,
            self._key_input,
            self._hotkey_display,
        ]:
            widget.setVisible(is_hotkey)

        self._trigger_input.setVisible(not is_hotkey)

    def _on_table_click(self, row: int, col: int) -> None:
        """Load row when clicked."""
        if 0 <= row < len(self._items):
            self._load_row(row)

    def _load_row(self, row: int) -> None:
        """Load row into editor."""
        item = self._items[row]
        self._editing_index = row

        self._type_combo.setCurrentText(item["kind"])
        self._on_type_changed()

        self._desc_input.setText(item["desc"])
        self._output_input.setText(item["output"])

        if item["kind"] == "Hotstring":
            self._trigger_input.setText(item["trigger"])
        else:
            trigger = item["trigger"]
            self._check_ctrl.setChecked("^" in trigger)
            self._check_alt.setChecked("!" in trigger)
            self._check_shift.setChecked("+" in trigger)
            self._check_win.setChecked("#" in trigger)
            self._check_capslock.setChecked("CapsLock" in trigger)

            key = trigger
            key = key.replace("CapsLock & ", "")
            for char in "^!+#":
                key = key.replace(char, "")
            self._key_input.setText(key)

            self._action_combo.setCurrentText(
                "Run Program/URL" if item.get("action") == "run" else "Send Text"
            )

    def _on_add_or_save(self) -> None:
        """Save item."""
        kind = self._type_combo.currentText()
        desc = self._desc_input.text()
        output = self._output_input.toPlainText()

        if kind == "Hotstring":
            trigger = self._trigger_input.text().upper().strip()
            if not trigger:
                self._set_status("Enter hotstring trigger.")
                return

            item = {
                "kind": "Hotstring",
                "trigger": trigger,
                "desc": desc,
                "output": output,
            }
        else:
            key = self._key_input.text().strip()
            if not key:
                self._set_status("Pick a key.")
                return

            helper = HotkeyDisplayHelper()
            trigger = helper.parse_display_to_hotkey(
                self._check_ctrl.isChecked(),
                self._check_alt.isChecked(),
                self._check_shift.isChecked(),
                self._check_win.isChecked(),
                self._check_capslock.isChecked(),
                key
            )

            action = "run" if self._action_combo.currentText() == "Run Program/URL" else "send"

            item = {
                "kind": "Hotkey",
                "trigger": trigger,
                "desc": desc,
                "output": output,
                "action": action,
            }

        if self._editing_index is not None:
            self._items[self._editing_index] = item
            self._editing_index = None
        else:
            self._items.append(item)

        self._save_all()
        self._populate_table()
        self._set_status("Saved.")

    def _on_delete(self) -> None:
        """Delete item."""
        selected = self._table.selectedIndexes()
        if not selected:
            self._set_status("Select a row to delete.")
            return

        row = selected[0].row()

        if (
            QMessageBox.question(
                self,
                "Confirm",
                "Delete this item?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            == QMessageBox.StandardButton.Yes
        ):
            self._items.pop(row)
            self._save_all()
            self._populate_table()
            self._set_status("Deleted.")

    def _populate_table(self) -> None:
        """Populate table."""
        self._table.setRowCount(len(self._items))

        helper = HotkeyDisplayHelper()

        for row, item in enumerate(self._items):
            kind = QTableWidgetItem(item["kind"])
            
            # Display formatted hotkey
            if item["kind"] == "Hotkey":
                trigger_display = helper.format_hotkey_for_display(item["trigger"])
            else:
                trigger_display = item["trigger"]
            
            trigger = QTableWidgetItem(trigger_display)
            desc = QTableWidgetItem(item["desc"])
            
            output = item["output"][:60].replace("\n", " ⏎ ")
            if len(item["output"]) > 60:
                output += "…"
            output_item = QTableWidgetItem(output)

            self._table.setItem(row, 0, kind)
            self._table.setItem(row, 1, trigger)
            self._table.setItem(row, 2, desc)
            self._table.setItem(row, 3, output_item)

        self._table.setColumnWidth(0, 80)
        self._table.setColumnWidth(1, 180)
        self._table.setColumnWidth(2, 200)
        self._table.setColumnWidth(3, 200)

    def _save_all(self) -> None:
        """Save to file."""
        config_dir = os.path.join(os.path.dirname(__file__), "..", "..", "config")
        os.makedirs(config_dir, exist_ok=True)

        hotkey_file = os.path.join(config_dir, "hotkeys.ini")
        hotstring_file = os.path.join(config_dir, "hotstrings.sav")

        with open(hotkey_file, "w") as f:
            for item in self._items:
                if item["kind"] == "Hotkey":
                    action = item.get("action", "send")
                    f.write(f'{item["trigger"]}|{item["desc"]}|{action}|{item["output"]}\n')

        with open(hotstring_file, "w") as f:
            for item in self._items:
                if item["kind"] == "Hotstring":
                    f.write(f':*C:{item["trigger"]}::{item["output"]}\n')

    def _load_all(self) -> None:
        """Load from file."""
        config_dir = os.path.join(os.path.dirname(__file__), "..", "..", "config")
        hotkey_file = os.path.join(config_dir, "hotkeys.ini")
        hotstring_file = os.path.join(config_dir, "hotstrings.sav")

        if os.path.exists(hotkey_file):
            with open(hotkey_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("|")
                    if len(parts) >= 4:
                        self._items.append({
                            "kind": "Hotkey",
                            "trigger": parts[0],
                            "desc": parts[1],
                            "action": parts[2],
                            "output": parts[3],
                        })

        if os.path.exists(hotstring_file):
            import re
            with open(hotstring_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    match = re.match(r"^:(?P<opts>.*?):(?P<abbr>.*?)::(?P<repl>.*)$", line)
                    if match:
                        self._items.append({
                            "kind": "Hotstring",
                            "trigger": match.group("abbr"),
                            "desc": "",
                            "output": match.group("repl"),
                        })

    def _set_status(self, msg: str) -> None:
        """Set status message."""
        self._status_label.setText(msg)

        if self._status_timer:
            self._status_timer.stop()

        self._status_timer = QTimer()
        self._status_timer.setSingleShot(True)
        self._status_timer.timeout.connect(lambda: self._status_label.setText("Ready."))
        self._status_timer.start(2500)

    def _apply_theme(self) -> None:
        """Apply dark theme."""
        stylesheet = """
            ImprovedHotkeysManagerWindow {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QLabel {
                color: #e0e0e0;
            }
            QLineEdit, QComboBox, QTextEdit {
                background-color: #252525;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                padding: 5px;
                border-radius: 3px;
                font-size: 11px;
            }
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {
                border: 1px solid #007acc;
            }
            QCheckBox {
                color: #e0e0e0;
                spacing: 8px;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #252525;
                border: 2px solid #3d3d3d;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                background-color: #007acc;
                border: 2px solid #007acc;
                border-radius: 3px;
                image: url(none);
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QGroupBox {
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 3px;
                padding: 10px;
                margin-top: 10px;
            }
            QTableWidget {
                background-color: #252525;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
            }
            QTableWidget::item {
                padding: 4px;
            }
            QTableWidget::item:selected {
                background-color: #007acc;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #e0e0e0;
                padding: 4px;
                border: none;
            }
        """
        self.setStyleSheet(stylesheet)


