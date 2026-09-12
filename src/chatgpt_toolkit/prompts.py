from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Prompt:
    """A reusable prompt template."""

    name: str
    template: str
    description: str = ""
    variables: list[str] = field(default_factory=list)

    def render(self, **kwargs: str) -> str:
        """Render the prompt template using keyword arguments."""

        missing = [
            variable
            for variable in self.variables
            if variable not in kwargs
        ]

        if missing:
            raise ValueError(
                f"Missing prompt variables: {', '.join(missing)}"
            )

        return self.template.format(**kwargs)


class PromptManager:
    """Manage reusable prompt templates."""

    def __init__(self) -> None:
        self._prompts: Dict[str, Prompt] = {}

    def add(self, prompt: Prompt) -> None:
        """Add or replace a prompt."""

        self._prompts[prompt.name] = prompt

    def get(self, name: str) -> Prompt:
        """Return a prompt by name."""

        try:
            return self._prompts[name]
        except KeyError as exc:
            raise KeyError(
                f"Prompt '{name}' was not found."
            ) from exc

    def remove(self, name: str) -> None:
        """Remove a prompt."""

        if name not in self._prompts:
            raise KeyError(f"Prompt '{name}' was not found.")

        del self._prompts[name]

    def list(self) -> list[str]:
        """Return all available prompt names."""

        return sorted(self._prompts.keys())

    def render(self, name: str, **kwargs: str) -> str:
        """Render a stored prompt."""

        return self.get(name).render(**kwargs)
