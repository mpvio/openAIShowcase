from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Message(BaseModel):
    role: str
    content: str
    refusal: Optional[str] = None
    reasoning: Optional[str] = None

class Choice(BaseModel):
    logprobs: Optional[Dict[str, Any]] = None
    finish_reason: str = Field(alias="finish_reason")  # Handles snake_case in JSON
    native_finish_reason: str
    index: int
    message: Message

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ResponseClass(BaseModel):
    id: str
    provider: str
    model: str
    object: str = Field(alias="object")  # 'object' is a reserved keyword in Python
    created: int
    choices: List[Choice]
    usage: Usage

    @classmethod
    def from_response(cls, response):
        """Parse a requests.Response directly into a Pydantic model."""
        return cls.model_validate(response.json())

    # Optional: Convert back to JSON
    def to_json(self) -> str:
        return self.model_dump_json(indent=2)