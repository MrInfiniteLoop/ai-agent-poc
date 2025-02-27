from typing import List, Dict, Callable

class Tool:
    def __init__(self, name: str, description: str, function: Callable, parameters: List[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self.function = function
        self.parameters = parameters if parameters else []