import unittest
import sys
import os

# Add the directory containing aiagent.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiagent import AIAgent, Tool

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AIAgent()

    def test_get_tools_api_specs(self):
        specs = self.agent.get_tools_api_specs()
        expected_specs = json.dumps([
            {
                "name": "time",
                "description": "Get the current time",
                "parameters": [{}]
            },
            {
                "name": "search",
                "description": "Search the web",
                "parameters": [{"name": "query", "type": "str", "description": "The search query"}]
            }
        ], indent=4)
        self.assertEqual(specs, expected_specs)

    def test_execute_tool(self):
        # Test executing a non-existent tool
        result = self.agent.execute_tool("non_existent_tool", {})
        self.assertEqual(result, "Tool not found")



if __name__ == '__main__':
    unittest.main()