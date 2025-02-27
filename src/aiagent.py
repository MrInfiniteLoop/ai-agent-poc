from typing import List, Dict
import datetime
import json
import parser
import prompts
from tool import Tool
from agent_memory import AgentMemory

class AIAgent:
    def __init__(self):
        self.tools: List[Tool] = []
        self.memory = AgentMemory()
        self.register_default_tools()

    def get_context(self) -> str:
        return self.memory.serialize()

    def register_tool(self, tool: Tool):
        self.tools.append(tool)

    def register_default_tools(self):
        def get_current_time():
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        def search_web(query: str):
            return f"Searching the web for: {query}"

        self.register_tool(Tool("time", "Get the current time", get_current_time, [{}]))
        self.register_tool(Tool("search", "Search the web", search_web, [{"name": "query", "type": "str", "description": "The search query"}]))

    def get_tools_api_specs(self) -> str:
        tools_specs = [{"name": tool.name, "description": tool.description, "parameters": tool.parameters} for tool in self.tools]
        return json.dumps(tools_specs, indent=4)

    def execute_tool(self, tool_name: str, parameters: Dict) -> str:
        for tool in self.tools:
            if tool.name == tool_name:
                try:
                    return tool.function(**parameters)
                except Exception as e:
                    return f"Error executing tool: {e}"
        return "Tool not found"

    def process_response(self, response: str) -> Dict:
        tools_request = parser.parse_tools_request(response)
        for call in tools_request["tool_calls"]:
            tool_name = call['tool']
            parameters = call['parameters']
            call['response'] = self.execute_tool(tool_name, parameters)
        return tools_request

    def get_retrieval_prompt(self, user_request: str) -> str:
        tools_api_specs = self.get_tools_api_specs()
        return prompts.get_retrieval_prompt(tools_api_specs, user_request)

    def get_interpretation_prompt(self, user_request: str, processed_response: Dict) -> str:
        return prompts.get_interpretation_prompt(user_request, processed_response)

    def add_agent_response(self, response: str):
        self.memory.add_interaction("agent", response)


