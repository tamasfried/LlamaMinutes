'''
Minimal Minutes by TamasFried
----------------
This script is a basic meeting minutes summariser that captures key points from a meeting transcript.
It uses:
    - CrewAI (for agent/task assignment)
    - LangChain (to connect to a local LLM)
    - Ollama model "llama3.2:1b" (small and fast for local testing)

Workflow:
    1. Load the meeting minutes as .txt or .docx file.
    2. Psas the text to a CrewAI agent. (Llama in this case).
    The Agent produces a structured summary of the meeting minutes, including:
        - Key decisions made
        - Action items assigned (with responsible persons)
        - Important discussion points
    4. Print the structured summary.

Running this basic script:
    python minimal_minutes.py minutes.txt
    OR
    python minimal_minutes.py minutes.docx
'''

# Basic Imports
import sys                  # For command line arguments
from pathlib import Path    # For file path handling

# External Libraries
from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama
try:
    import docx # For reading .docx files
except ImportError:
    docx = None # only needed if .docx files are used

# ----------------------
# File Loading Function
# ----------------------
def load_minutes(path_str: str) -> str:
    # Load text from a .txt or .docx file
    # Returns the content as a string.
    p = Path(path_str)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    