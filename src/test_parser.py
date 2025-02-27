import unittest
from parser import extract_tool_calls, interpret_tool_calls

class TestParser(unittest.TestCase):

    def test_extract_tool_calls(self):
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
        expected_tool_calls = [
            {
                "tool": "time",
                "parameters": {}
            }
        ]
        tool_calls = extract_tool_calls(response)
        print(tool_calls)
        self.assertEqual(tool_calls, expected_tool_calls)

if __name__ == '__main__':
    unittest.main()
