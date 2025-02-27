import json
from typing import Dict, List

def parse_tools_request(response: str) -> Dict:
    """ Extract tool calls from the JSON response string """
    try:
        # Extract the JSON part from the response
        start = response.find('{')
        end = response.rfind('}') + 1
        json_str = response[start:end]
        return json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        return {}
