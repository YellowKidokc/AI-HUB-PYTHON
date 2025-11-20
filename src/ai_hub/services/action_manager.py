"""WritingTools-style action management system."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from .openai_client import OpenAIClient


@dataclass
class Action:
    """Represents a WritingTools-style quick action."""

    name: str
    description: str
    prompt: str
    hotkey: Optional[str] = None
    icon: Optional[str] = None


class ActionManager:
    """Manages WritingTools-style quick actions."""

    def __init__(self, client: OpenAIClient):
        self._client = client
        self._actions: dict[str, Action] = {}
        self._setup_default_actions()

    def _setup_default_actions(self) -> None:
        """Setup WritingTools-style default actions."""
        self._actions["proofread"] = Action(
            name="Proofread",
            description="Fix grammar, spelling, and punctuation",
            prompt="Fix all grammar, spelling, and punctuation errors in this text. Return ONLY the corrected text, with no explanations.",
            hotkey="ctrl+shift+j",
        )

        self._actions["rewrite"] = Action(
            name="Rewrite",
            description="Improve clarity and flow",
            prompt="Rewrite this text to improve clarity and flow while keeping the same meaning. Return ONLY the rewritten text.",
            hotkey="ctrl+shift+r",
        )

        self._actions["friendly"] = Action(
            name="Make Friendly",
            description="Use a casual, friendly tone",
            prompt="Rewrite this text in a casual, friendly tone. Return ONLY the rewritten text.",
            hotkey="ctrl+shift+f",
        )

        self._actions["professional"] = Action(
            name="Make Professional",
            description="Use a formal, professional tone",
            prompt="Rewrite this text in a formal, professional tone. Return ONLY the rewritten text.",
            hotkey="ctrl+shift+p",
        )

        self._actions["summarize"] = Action(
            name="Summarize",
            description="Create a concise summary",
            prompt="Create a concise summary of this text. Return ONLY the summary.",
            hotkey="ctrl+shift+s",
        )

        self._actions["expand"] = Action(
            name="Expand",
            description="Make text longer and more detailed",
            prompt="Expand this text with more details and explanations. Return ONLY the expanded text.",
        )

        self._actions["simplify"] = Action(
            name="Simplify",
            description="Use simpler language",
            prompt="Simplify this text using simpler language while keeping the same meaning. Return ONLY the simplified text.",
        )

    def get_action(self, action_id: str) -> Optional[Action]:
        """Get an action by ID."""
        return self._actions.get(action_id)

    def get_all_actions(self) -> list[Action]:
        """Get all available actions."""
        return list(self._actions.values())

    def register_action(self, action_id: str, action: Action) -> None:
        """Register a custom action."""
        self._actions[action_id] = action

    async def execute_action(self, action_id: str, text: str) -> str:
        """Execute an action on the given text."""
        action = self.get_action(action_id)
        if not action:
            return f"Action '{action_id}' not found"

        try:
            result = self._client.chat(system=action.prompt, user=text, temperature=0.2)
            return result
        except Exception as e:
            return f"Error executing action: {str(e)}"

    def execute_action_sync(self, action_id: str, text: str) -> str:
        """Execute an action synchronously."""
        action = self.get_action(action_id)
        if not action:
            return f"Action '{action_id}' not found"

        result = self._client.chat(system=action.prompt, user=text, temperature=0.2)
        return result

