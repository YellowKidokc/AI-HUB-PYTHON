"""
Audio Engine for AI Hub - Voice capabilities (TTS + STT)

Uses:
- edge-tts: High-quality neural voices (Microsoft Azure)
- faster-whisper: Local speech-to-text (optimized Whisper)
"""

from __future__ import annotations

import asyncio
import os
from pathlib import Path
from typing import Optional

try:
    import edge_tts
    HAVE_EDGE_TTS = True
except ImportError:
    HAVE_EDGE_TTS = False

try:
    from faster_whisper import WhisperModel
    HAVE_WHISPER = True
except ImportError:
    HAVE_WHISPER = False

try:
    import pygame
    HAVE_PYGAME = True
except ImportError:
    HAVE_PYGAME = False

try:
    import sounddevice as sd
    import numpy as np
    import scipy.io.wavfile as wav
    HAVE_RECORDING = True
except ImportError:
    HAVE_RECORDING = False


# --- CONFIGURATION ---
RECORDING_FILE = "temp_recording.wav"
TTS_OUTPUT_FILE = "temp_speech.mp3"
WHISPER_MODEL_SIZE = "tiny"  # Options: tiny, base, small, medium, large
VOICE = "en-US-BrianMultilingualNeural"  # Brian - Multilingual, natural (DEFAULT)

# Popular voices:
# "en-US-BrianMultilingualNeural" - Brian, multilingual, natural (RECOMMENDED)
# "en-US-GuyNeural" - Deep, professional male
# "en-US-AriaNeural" - Female, friendly
# "en-GB-SoniaNeural" - British female
# "en-US-JennyNeural" - Female, warm
# "en-AU-NatashaNeural" - Australian female


class AudioEngine:
    """Handles TTS, STT, and audio recording."""

    def __init__(self, whisper_model_size: str = WHISPER_MODEL_SIZE, voice: str = VOICE):
        self.whisper_model_size = whisper_model_size
        self.voice = voice
        self.stt_model: Optional[WhisperModel] = None
        self._pygame_initialized = False
        
        # Check dependencies
        if not HAVE_EDGE_TTS:
            print("⚠️ edge-tts not installed. TTS will not work.")
            print("   Install: pip install edge-tts")
        
        if not HAVE_WHISPER:
            print("⚠️ faster-whisper not installed. STT will not work.")
            print("   Install: pip install faster-whisper")
        
        if not HAVE_PYGAME:
            print("⚠️ pygame not installed. Audio playback will not work.")
            print("   Install: pip install pygame")
        
        if not HAVE_RECORDING:
            print("⚠️ sounddevice/scipy not installed. Recording will not work.")
            print("   Install: pip install sounddevice scipy numpy")

    def initialize_whisper(self) -> bool:
        """Load Whisper model (call this in a background thread)."""
        if not HAVE_WHISPER:
            return False
        
        try:
            print(f"🎤 Loading Whisper Model ({self.whisper_model_size})...")
            # Run on CPU with INT8 quantization for speed
            self.stt_model = WhisperModel(
                self.whisper_model_size,
                device="cpu",
                compute_type="int8"
            )
            print("✅ Whisper Model Ready")
            return True
        except Exception as e:
            print(f"❌ Error loading Whisper: {e}")
            return False

    def initialize_pygame(self) -> bool:
        """Initialize pygame mixer for audio playback."""
        if not HAVE_PYGAME:
            return False
        
        if not self._pygame_initialized:
            try:
                pygame.mixer.init()
                self._pygame_initialized = True
                return True
            except Exception as e:
                print(f"❌ Error initializing pygame: {e}")
                return False
        return True

    # --- TEXT TO SPEECH (The Voice) ---
    def speak(self, text: str) -> bool:
        """
        Convert text to speech using high-quality Edge Neural voices.
        
        Args:
            text: The text to speak
            
        Returns:
            True if successful, False otherwise
        """
        if not HAVE_EDGE_TTS or not HAVE_PYGAME:
            print("⚠️ TTS dependencies not available")
            return False

        async def _generate():
            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save(TTS_OUTPUT_FILE)

        try:
            # Initialize pygame if needed
            if not self.initialize_pygame():
                return False

            # Generate speech file
            asyncio.run(_generate())
            
            # Play the audio
            pygame.mixer.music.load(TTS_OUTPUT_FILE)
            pygame.mixer.music.play()
            
            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            # Cleanup
            pygame.mixer.music.unload()
            
            # Remove temp file
            try:
                os.remove(TTS_OUTPUT_FILE)
            except:
                pass
            
            return True
            
        except Exception as e:
            print(f"❌ TTS Error: {e}")
            return False

    # --- SPEECH TO TEXT (The Ears) ---
    def transcribe_file(self, file_path: str) -> str:
        """
        Transcribe audio or video files to text.
        
        Supports: MP3, WAV, MP4, M4A, and more (via ffmpeg)
        
        Args:
            file_path: Path to audio/video file
            
        Returns:
            Transcribed text or error message
        """
        if not HAVE_WHISPER:
            return "❌ faster-whisper not installed"
        
        if not self.stt_model:
            return "❌ Whisper model not loaded. Call initialize_whisper() first."
        
        if not os.path.exists(file_path):
            return f"❌ File not found: {file_path}"

        try:
            print(f"🎤 Transcribing: {file_path}")
            segments, info = self.stt_model.transcribe(file_path, beam_size=5)
            
            full_text = ""
            print(f"   Detected language: '{info.language}' (confidence: {info.language_probability:.2f})")

            for segment in segments:
                full_text += segment.text + " "
            
            result = full_text.strip()
            print(f"✅ Transcription complete ({len(result)} characters)")
            return result
            
        except Exception as e:
            error_msg = f"❌ Error transcribing: {e}"
            print(error_msg)
            return error_msg

    # --- RECORDING ---
    def record_audio(self, duration: int = 5, samplerate: int = 44100) -> str:
        """
        Record audio from microphone.
        
        Args:
            duration: Recording duration in seconds
            samplerate: Sample rate (44100 is CD quality)
            
        Returns:
            Path to recorded file
        """
        if not HAVE_RECORDING:
            print("❌ Recording dependencies not available")
            return ""

        try:
            print(f"🎤 Recording for {duration} seconds...")
            recording = sd.rec(
                int(duration * samplerate),
                samplerate=samplerate,
                channels=1,
                dtype='int16'
            )
            sd.wait()  # Wait until recording is finished
            print("✅ Recording finished")
            
            wav.write(RECORDING_FILE, samplerate, recording)
            return RECORDING_FILE
            
        except Exception as e:
            print(f"❌ Recording error: {e}")
            return ""

    def get_available_voices(self) -> list[str]:
        """Get list of available Edge TTS voices."""
        if not HAVE_EDGE_TTS:
            return []
        
        try:
            # This is a synchronous wrapper around the async function
            async def _get_voices():
                voices = await edge_tts.list_voices()
                return [v["ShortName"] for v in voices if v["Locale"].startswith("en")]
            
            return asyncio.run(_get_voices())
        except Exception as e:
            print(f"❌ Error getting voices: {e}")
            return [VOICE]  # Return default

    def set_voice(self, voice: str) -> None:
        """Change the TTS voice."""
        self.voice = voice
        print(f"🔊 Voice changed to: {voice}")

    def pause_playback(self) -> bool:
        """Pause current audio playback."""
        if not HAVE_PYGAME or not self._pygame_initialized:
            return False
        try:
            pygame.mixer.music.pause()
            return True
        except:
            return False

    def resume_playback(self) -> bool:
        """Resume paused audio playback."""
        if not HAVE_PYGAME or not self._pygame_initialized:
            return False
        try:
            pygame.mixer.music.unpause()
            return True
        except:
            return False

    def stop_playback(self) -> bool:
        """Stop current audio playback."""
        if not HAVE_PYGAME or not self._pygame_initialized:
            return False
        try:
            pygame.mixer.music.stop()
            return True
        except:
            return False

    def is_playing(self) -> bool:
        """Check if audio is currently playing."""
        if not HAVE_PYGAME or not self._pygame_initialized:
            return False
        try:
            return pygame.mixer.music.get_busy()
        except:
            return False

    def cleanup(self) -> None:
        """Clean up temporary files."""
        for temp_file in [RECORDING_FILE, TTS_OUTPUT_FILE]:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass


# --- CONVENIENCE FUNCTIONS ---

def quick_speak(text: str, voice: str = VOICE) -> bool:
    """Quick function to speak text without creating an engine instance."""
    engine = AudioEngine(voice=voice)
    engine.initialize_pygame()
    return engine.speak(text)


def quick_transcribe(file_path: str, model_size: str = WHISPER_MODEL_SIZE) -> str:
    """Quick function to transcribe a file."""
    engine = AudioEngine(whisper_model_size=model_size)
    if engine.initialize_whisper():
        return engine.transcribe_file(file_path)
    return "❌ Failed to initialize Whisper"
