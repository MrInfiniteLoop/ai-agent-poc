
from typing import Dict

json_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["tool_calls", "plan"],
  "properties": {
    "tool_calls": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["tool", "parameters"],
        "properties": {
          "tool": {
            "type": "string"
          },
          "parameters": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        }
      }
    },
    "plan": {
      "type": "string"
    }
  }
}

def get_retrieval_prompt(tools_api_specs: str, user_request: str) -> str:
    return f"""# Retrieval Process

## System Prompt 
You are a preparing the data retrieval for a helpful assistant. 
You are getting a user request that the helpful assistant will need to answer.
You are getting a list of tools that you can use to perform tasks and to receive external data to augment your knowledge if needed.
You will analyze the user's request and respond nothing but a JSON object containing:
    * the tool calls and their parameters
    * A description of a plan how you will proceed after you received the results from the tools
Here is the JSON schema for your response:
```json
{json_schema}
```    

## User request
{user_request}


## Available tools API specs
```json
{tools_api_specs}
```
You shall only use the tools provided, do not invent new tools.

## Example
For a user question like "Summarize the latest news for me", the expected example JSON response:
```json
{{
    
    "tool_calls": [
        {{
            "tool": "search",
            "parameters": {{
                "query": "news"
            }}
        }},
    ],
    "plan": "I will summarize the news based on the search results."
}}
```
"""


def get_interpretation_prompt(user_request: str, processed_response: Dict) -> str:
    return f"""# Interpretation Process
## System Prompt
You are a helpful assistant. 
You are getting a user request that the helpful assistant will need to answer.
As preparation a retrieval process has been done and you have received the results.
You are expected to interpret the results and provide a response to the user.

## User request
{user_request}

## Results of the retrieval process
```json
{processed_response}
```
    """
