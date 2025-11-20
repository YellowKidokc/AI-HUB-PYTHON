from __future__ import annotations

import threading

from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QTextEdit, QHBoxLayout
from PySide6.QtCore import Qt

from ...services.openai_client import OpenAIClient
from ...services.prompt_manager import Prompt
from ...services.selection import get_selection, replace_selection
from ..tabs.base import BaseTab


class SpellingTab(BaseTab):
    def __init__(self, client: OpenAIClient, spelling_prompt: Prompt):
        super().__init__()
        self._client = client
        self._prompt = spelling_prompt
        self._text_edit = None
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Paste or type text to fix spelling:"))
        
        # Text editor
        self._text_edit = QTextEdit()
        self._text_edit.setPlaceholderText("Type or paste text here, then click Fix or press Ctrl+Alt+Spacebar")
        self._text_edit.setMinimumHeight(200)
        layout.addWidget(self._text_edit)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        fix_btn = QPushButton("Fix Spelling Now (Ctrl+Alt+Space)", self)
        fix_btn.clicked.connect(self._on_fix_clicked)
        btn_layout.addWidget(fix_btn)
        
        clear_btn = QPushButton("Clear", self)
        clear_btn.clicked.connect(lambda: self._text_edit.clear())
        btn_layout.addWidget(clear_btn)
        
        layout.addLayout(btn_layout)
        layout.addStretch(1)

    def _on_fix_clicked(self) -> None:
        """Fix spelling in the text field."""
        text = self._text_edit.toPlainText()
        
        if not text.strip():
            return

        # Save original for undo
        self._original_text = text
        
        def run() -> None:
            output = self._client.chat(
                self._prompt.system or None, 
                self._prompt.build_message(text), 
                self._prompt.temperature
            )
            if output.strip():
                # Update text field with fixed version
                self._text_edit.setPlainText(output)

        threading.Thread(target=run, daemon=True).start()

    def keyPressEvent(self, event) -> None:
        """Handle Ctrl+Alt+Spacebar hotkey."""
        # Check for Ctrl+Alt+Spacebar
        if (event.key() == Qt.Key.Key_Space and 
            event.modifiers() & Qt.KeyboardModifier.ControlModifier and
            event.modifiers() & Qt.KeyboardModifier.AltModifier):
            self._on_fix_clicked()
            event.accept()
        elif event.key() == Qt.Key.Key_Z and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            # Ctrl+Z for undo - built into QTextEdit
            self._text_edit.undo()
            event.accept()
        else:
            super().keyPressEvent(event)
