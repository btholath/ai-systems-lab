
# Python Basics

This module covers Python fundamentals, including variables, data structures, loops, and functions.

## Notebooks
- [Basics Notebook](./basics.ipynb): Introduction to Python syntax and basic operations.

## Getting Started
- Activate virtual env: `source .venv/bin/activate`
- Run Jupyter: `jupyter notebook`


created basics.ipynb in 01_python_basics, let’s ensure Jupyter is working correctly in Codespaces and that you can run notebooks.

Start Jupyter Notebook Server:
In the terminal (with .venv activated):
jupyter notebook

Look for the output with a URL like http://127.0.0.1:8888/?token=....
In Codespaces, this port is automatically forwarded. Click the "Ports" tab in VS Code (bottom panel) to see port 8888. If it’s not public, right-click it and set to "Public" (or use VS Code’s Jupyter interface).
Alternatively, open basics.ipynb directly in VS Code (it should detect the Jupyter extension installed via devcontainer.json).



Test the Notebook:

Open 01_python_basics/basics.ipynb in VS Code.
Add a test cell:
pythonprint("AI Systems Lab - Python Basics")
import numpy as np
print(np.__version__)

Run the cell (Shift+Enter or the "Run Cell" button in VS Code).
If it runs without errors and shows the NumPy version, your environment is set up correctly.
If you get errors (e.g., ModuleNotFoundError), ensure dependencies are installed:
textpip install -r requirements.txt

Save and Commit:
After adding content to basics.ipynb

git add 01_python_basics/basics.ipynb
git commit -m "Add initial content to basics.ipynb"
git push origin main

Check .github/workflows/ci.yml:
Your CI workflow looks like a linting setup with flake8. Ensure it’s functional by pushing a change and checking the Actions tab on GitHub (https://github.com/btholath/ai-systems-lab/actions). If you want to lint notebooks too, install nbqa:

pip install nbqa


Update ci.yml to lint notebooks:
name: CI
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - run: pip install flake8 nbqa
    - run: flake8 .
    - run: nbqa flake8 *.ipynb --extend-ignore=E402,E501


Step 3: Develop Content for 01_python_basics
Start populating basics.ipynb with educational content to set the tone for your lab. Here’s a suggested structure for basics.ipynb:
    