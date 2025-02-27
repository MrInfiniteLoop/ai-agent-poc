# AI Agent PoC

This project is a Jupyter Notebook application for a PoC on simple AI agents

## Project Structure

```
jupyter-notebook-app
├── notebooks
│   └── main.ipynb        # Jupyter Notebook for analysis
├── src
│   ├── __init__.py       # Package initialization
│   └── my_class.py       # Custom Python classes
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd jupyter-notebook-app
   ```

2. Activate your virtual environment:
   ```
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

2. Launch Jupyter Notebook:
   ```
   jupyter notebook notebooks/main.ipynb
   ```

3. Import your custom classes in the notebook:
   ```python
   from src.my_class import MyClass
   ```
