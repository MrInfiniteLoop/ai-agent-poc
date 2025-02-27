import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import parse_tools_request

class TestParser(unittest.TestCase):

    def test_parse_tools_request(self):
        response = """
        To assist with this user's request, I'll first analyze their query and then generate a JSON object containing the necessary tool calls.

        Here is my response:

        {
            "tool_calls": [
                {
                    "tool": "time",
                    "parameters": {}
                }
            ]
        }

        I need to run the `time` tool to get the current time. This will allow me to calculate when the user will arrive after a two-hour ride.
        """
        expected_tool_calls = {
            "tool_calls": [ {
                "tool": "time",
                "parameters": {}
            }
            ]
        }
        tool_calls = parse_tools_request(response)
        self.assertEqual(tool_calls, expected_tool_calls)


if __name__ == '__main__':
    unittest.main()
