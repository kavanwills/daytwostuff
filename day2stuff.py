#%%
# @kavanwills ➜ /workspaces/daytwostuff (main) $
#%%
# No, because you can use a requirements.txt file to give future users the requirements
# (.venv) @kavanwills ➜ /workspaces/daytwostuff (main) $ , so it now says (.venv) indicating an active virtual environment
#%%
import pandas as pd
x = pd.read_csv("penguins.csv")
#%%
# There is now a local section and a codespace section in the extension menu
# Visualize & filter large tabular datasets, one-click transforms (fill, drop, type-cast…), Automatic Pandas code preview & export
#%%
# We use a requirements.txt file to allow future users to access the necessary packages and versions.
#%%
# Recipe: Install necessary extensions in VS Code (Python, Data Wrangler, Jupyter, etc.), create a file (if .py add ipykernel for interactive), activate virtual environment in terminal, then make a requirements.txt file with any packages/versions you need. Finally, commit and push changes
# %%
# Terminal commands used:
# python -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# pip install plotly
# pip show plotly
# pip freeze > requirements.txt
# git status
# git add .
# git commit -m "Day 2 setup"
# git push
