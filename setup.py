"""
AI Hub Setup Script
Provides backward compatibility for pip install
"""
from setuptools import setup, find_packages

# Read dependencies from pyproject.toml
setup(
    name="ai-hub",
    version="0.2.0",
    description="AI-powered desktop hub with voice, shortcuts, chat, and automation",
    author="AI Hub",
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PySide6>=6.6,<7.0",
        "requests>=2.31",
        "keyboard>=0.13",
        "pynput>=1.8",
        "pyperclip>=1.8",
        "pyautogui>=0.9.54",
        "pywin32>=306; platform_system=='Windows'",
    ],
    extras_require={
        "voice": [
            "edge-tts>=6.1",
            "faster-whisper>=0.10",
            "sounddevice>=0.4",
            "scipy>=1.11",
            "numpy>=1.24",
            "pygame>=2.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-hub=ai_hub.app:main",
        ],
    },
)
