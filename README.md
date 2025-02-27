# AI Agent PoC

This project is a proof of concept for simple AI agents.

## Notebook Summary

The `ai_agent_poc.ipynb` notebook demonstrates how an AI agent can perform tasks and augment its knowledge using a tools construct to call Python methods. The notebook covers the following steps:

1. **Loading My AI Agent Lib**: Initializes the AI agent and loads necessary libraries.
2. **Generate The Retrieval Prompt**: Creates a prompt based on the user's request.
3. **Feed Prompt to LLM**: Sends the prompt to the language model and retrieves the response.
4. **Response Parsing & Processing**: Parses the response and executes the required tools.
5. **Generate Interpretation Prompt**: Creates a prompt to interpret the results.
6. **Feed Prompt to LLM**: Sends the interpretation prompt to the language model and retrieves the final response.

For more details, please refer to the [ai_agent_poc.ipynb](./notebooks/ai_agent_poc.ipynb) notebook.

## Project Structure

```
ai-agent-poc
├── src
│   ├── __init__.py
│   ├── aiagent.py
│   ├── agent_memory.py
│   ├── parser.py
│   ├── prompts.py
│   └── tool.py
├── tests
│   ├── __init__.py
│   ├── test_aiagent.py
│   └── test_parser.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-agent-poc
   ```

2. Create and activate your virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Activate your virtual environment:
   ```
   source venv/bin/activate
   ```

2. Run the tests:
   ```
   python -m unittest discover tests
   ```

3. Start the Jupyter Notebook:
   ```
   jupyter notebook
   ```

4. Open the `ai_agent_poc.ipynb` notebook and follow the step-by-step process to interact with the AI agent.


