import unittest
import sys
import os

# Add the directory containing aiagent.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiagent import AIAgent, Tool

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AIAgent()

    def test_get_tools_description(self):
        description = self.agent.get_tools_description()
        expected_description = (
            "Available Tools:\n\n"
            "- time: Get the current time\n"
            "- search: Search the web\n"
        )
        self.assertEqual(description, expected_description)


    def test_execute_tool(self):
        # Test executing the 'time' tool
        result = self.agent.execute_tool("time")
        self.assertTrue(result.startswith("Tool time result:"))

        # Test executing the 'search' tool
        query = "Python unittest"
        result = self.agent.execute_tool("search", query)
        self.assertEqual(result, f"Tool search result: Searching the web for: {query}")

        # Test executing a non-existent tool
        result = self.agent.execute_tool("non_existent_tool")
        self.assertEqual(result, "Tool not found")

    def test_extract_tool_calls(self):
        text = "<<time()>> and <<search(Python unittest)>>"
        expected_tool_calls = [
            {
                'tool': 'time',
                'parameters': '',
                'full_match': '<<time()>>'
            },
            {
                'tool': 'search',
                'parameters': 'Python unittest',
                'full_match': '<<search(Python unittest)>>'
            }
        ]
        tool_calls = self.agent.extract_tool_calls(text)
        self.assertEqual(tool_calls, expected_tool_calls)

if __name__ == '__main__':
    unittest.main()