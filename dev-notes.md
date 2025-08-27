
# Step 1: Verify Your Codespaces Environment
````bash
@btholath ➜ /workspaces/ai-systems-lab (main) $ tree
.
├── 01_python_basics
│   └── README.md
├── 02_data_science
│   └── README.md
├── 03_machine_learning_math
│   └── README.md
├── 04_probability_statistics
│   └── README.md
├── 05_machine_learning
│   └── README.md
├── 06_feature_engineering
│   └── README.md
├── 07_machine_learning_advanced
│   └── README.md
├── 08_model_tuning_optimization
│   └── README.md
├── 09_neural_network_and_deep_learning
│   └── README.md
├── 10_convolutional_neural_networks
│   └── README.md
├── 11_recurrent_neural_networks
│   └── README.md
├── 12_transformers_and_attention
│   └── README.md
├── 13_transfer_learning_and_fine_tuning
│   └── README.md
└── README.md
````

````bash
@btholath ➜ /workspaces/ai-systems-lab (main) $ ^C
@btholath ➜ /workspaces/ai-systems-lab (main) $ python --version
Python 3.12.1
@btholath ➜ /workspaces/ai-systems-lab (main) $ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
@btholath ➜ /workspaces/ai-systems-lab (main) $ 

git add .
git commit -m "Initial folder structure setup"
git push origin main
````

# Step 2: Create a Development Container Configuration (devcontainer.json)

Why? This makes your Codespaces environment reproducible. It defines the base image, extensions, and post-create commands (e.g., installing dependencies). It's stored in .devcontainer/devcontainer.json.
Actions:

In the root of your repo (/workspaces/ai-systems-lab), create a new folder and file
mkdir .devcontainer
touch .devcontainer/devcontainer.json

Open devcontainer.json in VS Code and paste the following configuration. This uses a Python 3.12 base image, installs the Jupyter VS Code extension, and sets up a virtual environment:
```bash
{
  "name": "AI Systems Lab",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-toolsai.jupyter",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "github.copilot"
      ]
    }
  },
  "postCreateCommand": "pip install --upgrade pip && pip install jupyter numpy pandas matplotlib scikit-learn torch torchvision",
  "remoteUser": "vscode"
}
```

# Explanation:
image: Base Docker image with Python 3.12.
extensions: Installs Jupyter support, Python IntelliSense, and optional Copilot for AI-assisted coding.
postCreateCommand: Installs core libraries needed across your AI/ML topics (e.g., NumPy for basics, PyTorch for deep learning). Expand this as needed.
Rebuild the Codespace: Click the Codespaces icon in the bottom-left of VS Code > "Rebuild Container". This applies the config and installs everything automatically.



# Step 3: Set Up a Virtual Environment

Why? Isolates dependencies to avoid conflicts, especially since your project spans many topics (e.g., basic Python vs. advanced ML libraries).
Actions:

In the terminal:
python -m venv .venv
source .venv/bin/activate

This creates and activates a virtual env in .venv.
Install Jupyter and initial dependencies (if not handled by devcontainer)
  pip install jupyter numpy pandas matplotlib scikit-learn torch torchvision

These cover basics for your folders (e.g., data science, ML, neural networks). For advanced topics like CNNs/RNNs, you can add more later (e.g., tensorflow if preferred over PyTorch).


Create a requirements.txt in the root for version control
touch requirements.txt
Open it and add:
jupyter>=1.0.0
numpy>=1.26.0
pandas>=2.2.0
matplotlib>=3.8.0
scikit-learn>=1.4.0
torch>=2.3.0
torchvision>=0.18.0
# Add more as needed, e.g., sympy for math, keras for DL

Install from it: pip install -r requirements.txt.

Add .venv to .gitignore to avoid committing the env
echo ".venv" >> .gitignore


# Step 4: Step 4: Configure Jupyter Notebooks in Codespaces
Why? Jupyter allows interactive coding, which is perfect for your lab's educational structure (e.g., running ML experiments in notebooks).

Actions:
Ensure the Jupyter extension is installed (from Step 2). In VS Code: Extensions sidebar > Search for "Jupyter" > Install if needed.
Start Jupyter Notebook server

jupyter notebook

This launches a server. In the terminal output, you'll see a URL like http://127.0.0.1:8888/?token=.... Copy it.
In VS Code, use "Jupyter: Enter the URL of a running server" (Ctrl+Shift+P > type "Jupyter: Enter").
Alternatively, for seamless integration, create a notebook directly: Right-click in a folder (e.g., 01_python_basics) > New File > Name it intro.ipynb.


Test it: Open intro.ipynb, add a cell with print("Hello, AI Lab!"), and run it (Shift+Enter).
For each folder, plan to add notebooks like:

01_python_basics/basics.ipynb for variables, loops, etc.
09_neural_network_and_deep_learning/feedforward.ipynb for NN implementations.
Update the folder's README.md with links, e.g., [Basics Notebook](./basics.ipynb)



# Step 5: Establish Best Practices and Project Hygiene
Why? As a software architect, I recommend structure for maintainability, especially for a multi-topic lab.
Actions:
Update the root README.md:
Open it and add
# AI Systems Lab

A comprehensive journey from Python basics to advanced AI/ML.

## Folder Structure
- 01_python_basics: Fundamentals of Python.
- ... (list all folders)

## Setup
- Use GitHub Codespaces for development.
- Activate virtual env: `source .venv/bin/activate`
- Run Jupyter: `jupyter notebook`

## Contributing
Add notebooks, commit changes, and push.


Commit your changes
git add .
git commit -m "Initial setup: devcontainer, venv, requirements, Jupyter config"
git push origin main

For data-heavy topics (e.g., datasets in 05_machine_learning), create a data/ subfolder in relevant directories and add to .gitignore if large.
Security: Avoid hardcoding secrets in notebooks; use environment variables if needed (e.g., for API keys in advanced ML).
Testing: For code in notebooks, extract reusable functions into .py files and add unit tests using pytest (install via pip install pytest).


# SECTION: 01_python_basics
# 01_python_basics/README.md
# Python Basics
