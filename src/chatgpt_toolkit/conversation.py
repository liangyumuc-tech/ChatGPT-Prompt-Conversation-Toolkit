from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal


Role = Literal["system", "user", "assistant"]


@dataclass
class Message:
    """A single conversation message."""

    role: Role
    content: str
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class Conversation:
    """Store and manage a conversation."""

    def __init__(
        self,
        system_prompt: str | None = None,
    ) -> None:
        self.messages: list[Message] = []

        if system_prompt:
            self.add_message("system", system_prompt)

    def add_message(
        self,
        role: Role,
        content: str,
    ) -> Message:
        """Add a message to the conversation."""

        if not content.strip():
            raise ValueError("Message content must not be empty.")

        message = Message(
            role=role,
            content=content,
        )

        self.messages.append(message)

        return message

    def add_user_message(self, content: str) -> Message:
        """Add a user message."""

        return self.add_message("user", content)

    def add_assistant_message(self, content: str) -> Message:
        """Add an assistant message."""

        return self.add_message("assistant", content)

    def clear(self) -> None:
        """Remove all messages."""

        self.messages.clear()

    def last_message(self) -> Message | None:
        """Return the most recent message."""

        if not self.messages:
            return None

        return self.messages[-1]

    def to_dict(self) -> list[dict]:
        """Convert the conversation to dictionaries."""

        return [
            {
                "role": message.role,
                "content": message.content,
                "timestamp": message.timestamp.isoformat(),
            }
            for message in self.messages
        ]

    def to_markdown(self) -> str:
        """Export the conversation as Markdown."""

        sections: list[str] = []

        for message in self.messages:
            role = message.role.capitalize()

            sections.append(
                f"## {role}\n\n{message.content}"
            )

        return "\n\n".join(sections)
