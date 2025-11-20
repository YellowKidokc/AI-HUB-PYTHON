from __future__ import annotations

from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox, QSystemTrayIcon, QTabWidget

from ..config import AppSettings
from ..hotkeys.global_hotkeys import GlobalHotkeys, HotkeyCallbacks
from ..hotkeys.hotstrings import AIHotstrings, HotstringEngine
from ..services.openai_client import OpenAIClient
from ..services.prompt_manager import Prompt, default_prompts
from ..services.window_manager import get_window_settings
from ..ui.tabs.audio_tab import AudioTab
from ..ui.tabs.chat_tab import ChatTab
from ..ui.tabs.prompts_tab import PromptsTab
from ..ui.tabs.prompts_manager_tab import PromptsManagerTab
from ..ui.tabs.settings_tab import SettingsTab
from ..ui.tabs.shortcuts_manager_tab import ShortcutsManagerTab
from ..ui.tabs.spelling_tab import SpellingTab
from ..ui.tabs.search_scraper_tab import SearchScraperTab
from ..ui.widgets.window_control_panel import WindowControlPanel
from ..ui.windows.clipboard_window import ClipboardWindow
from ..services.clipboard_hotkeys import ClipboardHotkeyService
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self, settings: AppSettings):
        super().__init__()
        self.setWindowTitle("AI Hub")
        self.resize(1000, 720)

        # Apply dark theme using native PySide6 stylesheet
        self._apply_dark_theme()

        self._settings = settings
        self._client = OpenAIClient(settings.openai)
        
        # Show warning if API key is missing
        if not settings.openai.api_key or settings.openai.api_key.startswith("sk-your"):
            QMessageBox.critical(
                self,
                "🔑 OpenAI API Key Required",
                "⚠️ Your OpenAI API key is NOT configured!\n\n"
                "❌ Without a key, AI features won't work:\n"
                "   • Chat, Spelling, Prompts\n"
                "   • AI Shortcuts & Hotstrings\n"
                "   • Ctrl+Space, Ctrl+Alt+P hotkeys\n\n"
                "✅ To fix this:\n"
                "1. Get API key: https://platform.openai.com/api-keys\n"
                "2. Edit 'settings.ini' in this folder\n"
                "3. Replace 'sk-your-api-key-here' with your real key\n"
                "4. Restart AI Hub\n\n"
                "📖 See SETUP_API_KEY.md for detailed instructions\n\n"
                "The API key is UNIVERSAL - it unlocks ALL AI features!"
            )
        self._prompts = list(default_prompts())
        self._tabs = QTabWidget(self)
        self.setCentralWidget(self._tabs)

        # Window manager (create early so it can be passed to tabs)
        self.window_settings = get_window_settings()
        self.window_control_panel = WindowControlPanel()
        
        self._chat_tab = ChatTab(self._client)
        self._prompts_manager_tab = PromptsManagerTab(self._client)  # New manager
        self._prompts_tab = PromptsTab(self._client, self._prompts)  # Keep old for compatibility
        self._spelling_tab = SpellingTab(self._client, self._prompts[0])
        self._shortcuts_tab = ShortcutsManagerTab(self._client, self._prompts)
        self._audio_tab = AudioTab(self.window_control_panel)
        self._search_tab = SearchScraperTab()
        self._settings_tab = SettingsTab()

        self._tabs.addTab(self._chat_tab, "💬 Chat")
        self._tabs.addTab(self._audio_tab, "🎙️ Voice")
        self._tabs.addTab(self._search_tab, "🔍 Search")
        self._tabs.addTab(self._shortcuts_tab, "⚡ Shortcuts")
        self._tabs.addTab(self._prompts_manager_tab, "📝 Prompts")  # New manager as main tab
        self._tabs.addTab(self._spelling_tab, "✏️ Spelling")
        self._tabs.addTab(self._settings_tab, "⚙️ Settings")

        self._tabs.currentChanged.connect(self._on_tab_changed)

        self._hotkeys = GlobalHotkeys(
            client=self._client,
            prompts=self._prompts,
            spelling_prompt=self._prompts[0],
            callbacks=HotkeyCallbacks(focus_hub_tab=self.focus_hub_tab),
            prompt_hotkey=settings.hotkeys.prompt_navigator,
            spelling_hotkey=settings.hotkeys.spelling,
            goto_hotkey=settings.hotkeys.goto_hub,
        )
        self._hotkeys.start()

        self._hotstrings_engine = HotstringEngine(
            buffer_size=settings.hotstrings.buffer_size,
            enabled=settings.hotstrings.enabled_by_default,
        )
        self._register_default_hotstrings()
        self._hotstrings_engine.start()

        keyboard = __import__("keyboard")
        keyboard.add_hotkey(
            settings.hotkeys.toggle_hotstrings,
            self._toggle_hotstrings,
            suppress=False,
            trigger_on_release=True,
        )
        
        # Register TTS hotkey (CapsLock+A)
        # Note: CapsLock acts as a modifier when held down
        try:
            keyboard.add_hotkey(
                "capslock+a",
                self._trigger_tts_from_selection,
                suppress=False,
                trigger_on_release=True,
            )
            print("✅ TTS Hotkey registered: CapsLock+A")
        except Exception as e:
            print(f"⚠️ Could not register TTS hotkey: {e}")
        
        # Register Ctrl+Alt+G hotkey to show/hide main window
        try:
            keyboard.add_hotkey(
                "ctrl+alt+g",
                self.toggle_window_visibility,
                suppress=False,
                trigger_on_release=True,
            )
            print("✅ Window Toggle Hotkey registered: Ctrl+Alt+G")
        except Exception as e:
            print(f"⚠️ Could not register window toggle hotkey: {e}")
        
        # Clipboard Manager
        clipboard_storage = Path("config/clipboard_history.json")
        self._clipboard_window = ClipboardWindow(clipboard_storage)
        self._clipboard_hotkey_service = ClipboardHotkeyService(self._clipboard_window.manager)
        self._clipboard_hotkey_service.register_all()
        
        # Register Ctrl+Alt+C hotkey to show clipboard manager
        try:
            keyboard.add_hotkey(
                "ctrl+alt+c",
                self._show_clipboard_manager,
                suppress=False,
                trigger_on_release=True,
            )
            print("✅ Clipboard Manager Hotkey registered: Ctrl+Alt+C")
        except Exception as e:
            print(f"⚠️ Could not register clipboard manager hotkey: {e}")
        
        # Connect window manager signals
        self.window_control_panel.always_on_top_changed.connect(self._apply_always_on_top)
        self.window_control_panel.save_position_requested.connect(self._save_window_positions)
        self.window_control_panel.save_size_requested.connect(self._save_window_sizes)
        
        # System tray icon
        self._setup_system_tray()
        
        # Load saved window geometry
        self._load_window_geometry()

    def _apply_dark_theme(self) -> None:
        """Apply native dark theme using PySide6 stylesheet."""
        dark_stylesheet = """
            QMainWindow {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QTabWidget::pane {
                border: 1px solid #3d3d3d;
            }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #e0e0e0;
                padding: 5px 15px;
                border: 1px solid #3d3d3d;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #404040;
                border-bottom: 2px solid #007acc;
            }
            QTabBar::tab:hover {
                background-color: #363636;
            }
            QLineEdit, QTextEdit, QPlainTextEdit {
                background-color: #252525;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                padding: 5px;
                border-radius: 3px;
            }
            QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
                border: 1px solid #007acc;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                padding: 6px 16px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
            QLabel {
                color: #e0e0e0;
            }
            QComboBox {
                background-color: #252525;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                padding: 5px;
                border-radius: 3px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #252525;
                color: #e0e0e0;
                selection-background-color: #007acc;
            }
            QScrollBar:vertical {
                background-color: #1e1e1e;
                width: 12px;
            }
            QScrollBar::handle:vertical {
                background-color: #505050;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #606060;
            }
            QMessageBox {
                background-color: #1e1e1e;
            }
            QMessageBox QLabel {
                color: #e0e0e0;
            }
        """
        self.setStyleSheet(dark_stylesheet)

    def _register_default_hotstrings(self) -> None:
        import time

        self._hotstrings_engine.register_text(";sig", "Best regards,\nYour Name")
        self._hotstrings_engine.register_text(";date", lambda: time.strftime("%Y-%m-%d"))
        self._hotstrings_engine.register_text(";time", lambda: time.strftime("%H:%M"))

        ai_hotstrings = AIHotstrings(self._client, self._prompts)
        self._hotstrings_engine.register_ai(";fix", ai_hotstrings.make_handler(0))
        self._hotstrings_engine.register_ai(";clar", ai_hotstrings.make_handler(1))
        self._hotstrings_engine.register_ai(";short", ai_hotstrings.make_handler(2))
        self._hotstrings_engine.register_ai(";long", ai_hotstrings.make_handler(3))

    def focus_hub_tab(self) -> None:
        self.show()
        self.raise_()
        self.activateWindow()
        self._tabs.setCurrentIndex(0)

    def _toggle_hotstrings(self) -> None:
        new_state = not self._hotstrings_engine.enabled
        self._hotstrings_engine.set_enabled(new_state)
        from PySide6.QtWidgets import QMessageBox

        QMessageBox.information(self, "AI Hub", f"Hotstrings {'enabled' if new_state else 'disabled'}.")

    def _trigger_tts_from_selection(self) -> None:
        """Trigger TTS from selected text (Ctrl+CapsLock+A hotkey)."""
        # Check if audio tab has engine ready
        if hasattr(self._audio_tab, 'engine') and self._audio_tab.engine:
            from ..services.tts_hotkey import TTSHotkeyService
            
            # Create TTS service with floating player
            tts_service = TTSHotkeyService(
                self._audio_tab.engine,
                self._audio_tab.floating_player
            )
            
            # Speak the selection
            tts_service.speak_selection()
        else:
            print("⚠️ Audio engine not ready yet")
    
    def _show_clipboard_manager(self) -> None:
        """Show clipboard manager window (Ctrl+Alt+C hotkey)."""
        self._clipboard_window.show()
        self._clipboard_window.raise_()
        self._clipboard_window.activateWindow()

    def _on_tab_changed(self, index: int) -> None:  # pragma: no cover - UI hook
        for i in range(self._tabs.count()):
            widget = self._tabs.widget(i)
            if hasattr(widget, "on_activate"):
                if i == index:
                    widget.on_activate()
                else:
                    widget.on_deactivate()

    def _setup_system_tray(self) -> None:
        """Setup system tray icon."""
        self.tray_icon = QSystemTrayIcon(self)
        
        # Use a visible system icon
        icon = self.style().standardIcon(self.style().SP_ComputerIcon)
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("AI Hub - Hotkeys Active\nClick to show window")
        
        # Create tray menu
        tray_menu = QMenu()
        
        show_action = QAction("🏠 Show AI Hub", self)
        show_action.triggered.connect(self.show_and_raise)
        tray_menu.addAction(show_action)
        
        clipboard_action = QAction("📋 Clipboard Manager", self)
        clipboard_action.triggered.connect(self._show_clipboard_manager)
        tray_menu.addAction(clipboard_action)
        
        window_manager_action = QAction("🎮 Window Manager", self)
        window_manager_action.triggered.connect(self.window_control_panel.show)
        tray_menu.addAction(window_manager_action)
        
        tray_menu.addSeparator()
        
        quit_action = QAction("❌ Exit AI Hub (stops hotkeys)", self)
        quit_action.triggered.connect(QApplication.quit)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        
        # Click to show
        self.tray_icon.activated.connect(self._on_tray_activated)
        
        self.tray_icon.show()
        print("✅ System tray icon created")

    def _on_tray_activated(self, reason) -> None:
        """Handle tray icon activation."""
        if reason == QSystemTrayIcon.Trigger:  # Left click
            self.show_and_raise()

    def show_and_raise(self) -> None:
        """Show and raise the main window."""
        self.show()
        self.raise_()
        self.activateWindow()

    def toggle_window_visibility(self) -> None:
        """Toggle main window visibility (Ctrl+Alt+G)."""
        if self.isVisible():
            self.hide()
        else:
            self.show_and_raise()

    def _load_window_geometry(self) -> None:
        """Load saved window geometry."""
        settings = self.window_settings.get_window_settings("main_window")
        
        if settings:
            x = settings.get("x", 100)
            y = settings.get("y", 100)
            width = settings.get("width", 1000)
            height = settings.get("height", 720)
            
            self.setGeometry(x, y, width, height)
            print(f"✅ Loaded window geometry: {x},{y} {width}x{height}")
        
        # Apply always-on-top if enabled
        if self.window_settings.is_always_on_top("main_window"):
            self._set_always_on_top(True)

    def _save_window_positions(self) -> None:
        """Save current window positions."""
        # Save main window
        pos = self.pos()
        self.window_settings.save_window_position("main_window", pos.x(), pos.y())
        
        # Save floating player if exists
        if hasattr(self._audio_tab, 'floating_player') and self._audio_tab.floating_player:
            player_pos = self._audio_tab.floating_player.pos()
            self.window_settings.save_window_position("floating_player", player_pos.x(), player_pos.y())
        
        print("💾 Window positions saved!")

    def _save_window_sizes(self) -> None:
        """Save current window sizes."""
        # Save main window
        size = self.size()
        self.window_settings.save_window_size("main_window", size.width(), size.height())
        
        # Floating player has fixed size, no need to save
        
        print("💾 Window sizes saved!")

    def _apply_always_on_top(self, enabled: bool) -> None:
        """Apply always-on-top setting to all windows."""
        # Apply to main window
        if self.window_settings.is_always_on_top("main_window"):
            self._set_always_on_top(True)
        else:
            self._set_always_on_top(False)
        
        # Apply to floating player
        if hasattr(self._audio_tab, 'floating_player') and self._audio_tab.floating_player:
            player = self._audio_tab.floating_player
            if self.window_settings.is_always_on_top("floating_player"):
                player.setWindowFlags(player.windowFlags() | Qt.WindowStaysOnTopHint)
            else:
                player.setWindowFlags(player.windowFlags() & ~Qt.WindowStaysOnTopHint)
            player.show()  # Need to show again after changing flags
        
        print(f"🎮 Always-on-top updated")

    def _set_always_on_top(self, enabled: bool) -> None:
        """Set always-on-top for main window."""
        if enabled:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()  # Need to show again after changing flags

    def closeEvent(self, event) -> None:
        """Handle window close event - minimize to tray instead of closing."""
        # Save geometry
        pos = self.pos()
        size = self.size()
        self.window_settings.save_window_geometry("main_window", pos.x(), pos.y(), size.width(), size.height())
        
        # Save floating player position if exists
        if hasattr(self._audio_tab, 'floating_player') and self._audio_tab.floating_player:
            player_pos = self._audio_tab.floating_player.pos()
            self.window_settings.save_window_position("floating_player", player_pos.x(), player_pos.y())
        
        # Minimize to tray instead of closing
        event.ignore()
        self.hide()
        
        # Show tray notification on first minimize
        if not hasattr(self, '_tray_notification_shown'):
            self.tray_icon.showMessage(
                "AI Hub",
                "App minimized to system tray. Hotkeys still work!\nRight-click tray icon to quit.",
                QSystemTrayIcon.Information,
                2000
            )
            self._tray_notification_shown = True


def run_app(settings: AppSettings) -> None:
    app = QApplication.instance() or QApplication([])
    window = MainWindow(settings)
    window.show()
    app.exec()
