import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
print("I AM IN VIS")

file_path = sys.argv[1]

df = pd.read_csv(file_path)

sns.histplot(df, x="citizenship")
plt.savefig("vis.png")


print("Visualization created and saved as vis.png.")

next_script = "model.py"
cmd = f"python3 {next_script} {file_path}"
os.system(cmd)
