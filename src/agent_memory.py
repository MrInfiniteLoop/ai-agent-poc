from typing import List, Dict

class AgentMemory:
    def __init__(self):
        self.conversations: List[Dict] = []

    def add_interaction(self, role: str, content: str):
        self.conversations.append({'role': role, 'content': content})

    def get_last_interaction(self, n: int = 5) -> str:
        recent = self.conversations[-n:] if len(self.conversations) > n else self.conversations
        context = ""
        for interaction in recent:
            context += f"{interaction['role']}: {interaction['content']}\n"
        return context

    def serialize(self) -> str:
        serialized = ""
        for c in self.conversations:
            if c['role'] == "system":
                serialized += f"{c['content']}\n\n"
            elif c['role'] == "user":
                serialized += f"USER: {c['content']}\n"
            elif c['role'] == "agent":
                serialized += f"ASSISTANT: {c['content']}\n"
        serialized += "ASSISTANT:"
        return serialized