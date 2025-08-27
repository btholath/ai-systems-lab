
# Issue with Git LFS not found on path
(.venv) @btholath ➜ /workspaces/ai-systems-lab (main) $ git add .

(.venv) @btholath ➜ /workspaces/ai-systems-lab (main) $ git commit -m "Add setup files: devcontainer, requirements, gitignore, README"

(.venv) @btholath ➜ /workspaces/ai-systems-lab (main) $ git push origin main

This repository is configured for Git LFS but 'git-lfs' was not found on your path. If you no longer wish to use Git LFS, remove this hook by deleting the 'pre-push' file in the hooks directory (set by 'core.hookspath'; usually '.git/hooks').

error: failed to push some refs to 'https://github.com/btholath/ai-systems-lab'

(.venv) @btholath ➜ /workspaces/ai-systems-lab (main) $ 

Step-by-Step Resolution
Step 1: Fix the Git LFS Issue
The error suggests Git LFS is configured but not installed. Since your project (based on the folder structure) doesn’t explicitly mention large files (e.g., datasets for ML), you can disable the LFS hook unless you plan to use it later.

Option 1: Disable Git LFS Hook
If you don’t need Git LFS now:

Remove the pre-push hook as suggested in the error:
rm .git/hooks/pre-push

Try pushing again:
git push origin main

If this works, your prior commit will be pushed, and the branch will be in sync.


Option 2: Install Git LFS
If you plan to use Git LFS (e.g., for large datasets in 05_machine_learning or 09_neural_network_and_deep_learning):

Install Git LFS in Codespaces:
sudo apt update
sudo apt install git-lfs
git lfs install
git lfs update --force

Track large files (if needed, e.g., for .csv, .h5, or model weights):
git lfs track "*.csv" "*.h5"
git add .gitattributes

Commit and push:
git commit -m "Add Git LFS configuration"
git push origin main

Recommendation: Since your project is primarily Jupyter Notebooks and small files at this stage, disable the hook (Option 1) for simplicity. Re-enable LFS later if you add large datasets.


# 