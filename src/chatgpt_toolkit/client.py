from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI


class ChatGPTClient:
    """Simple client for interacting with OpenAI models."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-5.6",
    ) -> None:
        """Create a ChatGPT client."""

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. "
                "Set the OPENAI_API_KEY environment variable "
                "or pass api_key explicitly."
            )

        self.model = model
        self.client = OpenAI(api_key=self.api_key)

    def ask(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """Send a prompt to the OpenAI model and return the response."""

        if not prompt.strip():
            raise ValueError("Prompt must not be empty.")

        instructions = system_prompt or (
            "You are a helpful and precise assistant."
        )

        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=prompt,
        )

        return response.output_text
