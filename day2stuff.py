#%%
# /workspaces/daytwostuff
#%%
# No, because you can use a requirements.txt file to give future users the requirements
# The display path is not different.
#%%
import pandas as pd
x = pd.read_csv("penguins.csv")
#%%
# There is now a local section and a codespace section in the extension menu
# Visualize & filter large tabular datasets, one-click transforms (fill, drop, type-cast…), Automatic Pandas code preview & export
#%%
# We use a requirements.txt file to allow future users to access the necessary packages and versions.
#%%
# Recipe: Install necessary extensions in VS Code (Python, Data Wrangler, Jupyter, etc.), create a file (if .py add ipykernel for interactive), activate virtual environment in terminal, then make a requirements.txt file with any packages/versions you need
# %%
