from typing import List, Dict, Callable
import datetime
import re
import json
import parser
import prompts

class Tool:
    def __init__(self, name: str, description: str, function: Callable, parameters: List[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self.function = function
        self.parameters = parameters if parameters else []

class AgentMemory:
    def __init__(self):
        self.conversations: List[Dict] = []

    def add_interaction(self, role:str, content:str):
        self.conversations.append({
            'role': role,
            'content': content
        })

    def get_last_interaction(self, n:int = 5) -> str:
        recent = self.conversations[-n:] if len(self.conversations) > n else self.conversations
        context = ""
        for interaction in recent:
            context += f"{interaction['role']}: {interaction['message']}\n"
        return context
    
    def serialize(self) -> str:
        serialized = ""
        for c in self.conversations:
            if(c['role'] == "system"):
                serialized += f"{c['content']}\n\n"
            elif(c['role'] == "user"):
                serialized += f"USER: {c['content']}\n"
            elif(c['role'] == "agent"):
                serialized += f"ASSISTANT: {c['content']}\n"
        serialized += f"ASSISTANT:"
        return serialized

class AIAgent:
    def __init__(self):
        self.tools: List[Tool] = []
        self.register_default_tools()
        self.memory = AgentMemory()

    def get_context(self) -> str:
        return self.memory.serialize()

    def register_tool(self, tool: Tool):
        self.tools.append(tool)

    def register_default_tools(self):
        """ Register the default tools """
        def get_current_time():
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        def search_web(query: str):
            return f"Searching the web for: {query}"
        
        self.register_tool(Tool("time", "Get the current time", get_current_time, [{}]))
        self.register_tool(Tool("search", "Search the web", search_web, [{"name": "query", "type": "str", "description": "The search query"}]))

    def get_tools_description(self) -> str:
        """ Get a description of the available tools """
        description = ""
        for tool in self.tools:
            description += f"- {tool.name}: {tool.description}\n"
        return description
    
    def get_tools_api_specs(self) -> str:
        """ Get a JSON representation of the tools API specs """
        tools_specs = []
        for tool in self.tools:
            tool_spec = {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters
            }
            tools_specs.append(tool_spec)
        return json.dumps(tools_specs, indent=4)

    def execute_tool(self, tool_name: str, parameters: Dict) -> str:
        """ Execute a tool by name with parameters """
        for tool in self.tools:
            if tool.name == tool_name:
                try:
                    result = tool.function(**parameters)
                    return f"{result}"
                except Exception as e:
                    return f"Error executing tool: {e}"
        return "Tool not found"

    def process_response(self, response:str) -> str:
        """ Process the JSON response, extracting and executing tool calls """
        tools_request = parser.parse_tools_request(response)
        for call in tools_request["tool_calls"]:
            tool_name = call['tool']
            parameters = call['parameters']
            call['response'] = self.execute_tool(tool_name, parameters)
        return tools_request

    def get_retrieval_prompt(self, user_request: str) -> str:
        """ Create a retrieval prompt for the user """
        tools_api_specs = self.get_tools_api_specs()
        return prompts.get_retrieval_prompt(tools_api_specs, user_request)
    
    def get_interpretation_prompt(self, user_request: str, processed_response: Dict) -> str:
        """ Create a interpretation prompt for the user """
        return prompts.get_interpretation_prompt(user_request, processed_response)


    def add_agent_response(self, response: str) -> str:
        """ Create a response for the user """
        self.memory.add_interaction("agent", response)


