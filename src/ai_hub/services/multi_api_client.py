"""Multi-API client supporting OpenAI, Claude (Anthropic), and more."""

from __future__ import annotations

from typing import Optional, Literal
import requests


class MultiAPIClient:
    """Unified client for multiple AI APIs."""

    def __init__(
        self,
        provider: Literal["openai", "claude", "custom"] = "openai",
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        endpoint: Optional[str] = None,
    ):
        """Initialize multi-API client."""
        self.provider = provider
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint
        self.timeout = 120

        # Set defaults based on provider
        if provider == "openai" and not model:
            self.model = "gpt-4o-mini"
            self.endpoint = "https://api.openai.com/v1/chat/completions"
        elif provider == "claude" and not model:
            self.model = "claude-3-5-sonnet-20241022"
            self.endpoint = "https://api.anthropic.com/v1/messages"

    def chat(self, system: Optional[str], user: str, temperature: float = 0.2) -> str:
        """Send chat message."""
        if not self.api_key:
            return "Missing API key for provider: " + self.provider

        if self.provider == "openai":
            return self._openai_chat(system, user, temperature)
        elif self.provider == "claude":
            return self._claude_chat(system, user, temperature)
        else:
            return "Unknown provider: " + self.provider

    def _openai_chat(self, system: Optional[str], user: str, temperature: float) -> str:
        """OpenAI API call."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": user})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                self.endpoint,
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()

            choices = data.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "No response")
            return "No choices in response"
        except Exception as e:
            return f"OpenAI error: {str(e)}"

    def _claude_chat(self, system: Optional[str], user: str, temperature: float) -> str:
        """Claude (Anthropic) API call."""
        messages = [{"role": "user", "content": user}]

        payload = {
            "model": self.model,
            "max_tokens": 1024,
            "messages": messages,
            "temperature": temperature,
        }

        if system:
            payload["system"] = system

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        try:
            response = requests.post(
                self.endpoint,
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()

            content = data.get("content", [])
            if content:
                return content[0].get("text", "No response")
            return "No content in response"
        except Exception as e:
            return f"Claude error: {str(e)}"

    @staticmethod
    def list_providers() -> list[str]:
        """List available providers."""
        return ["openai", "claude", "custom"]

    @staticmethod
    def get_default_models(provider: str) -> list[str]:
        """Get default models for provider."""
        models = {
            "openai": [
                "gpt-4",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-3.5-turbo",
            ],
            "claude": [
                "claude-3-5-sonnet-20241022",
                "claude-3-opus-20240229",
                "claude-3-sonnet-20240229",
                "claude-3-haiku-20240307",
            ],
        }
        return models.get(provider, [])


