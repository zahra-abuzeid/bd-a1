import pandas as pd
import os
import sys
print("I AM IN EDA")
file_path = sys.argv[1]
df = pd.read_csv(file_path)
insights = []
mean_age = int(df['age'].mean())
insights.append(f"The mean age is {mean_age} years")
unique_citizenship_values = df['citizenship'].unique()
insights.append(f"There are {len(unique_citizenship_values)} unique citizenship values")
count = df['gender'].value_counts()
mode_gender = df['gender'].mode().iloc[0]
insights.append(f"The mode gender in the dataset is: {mode_gender} at {count[0]}")
for i, insight in enumerate(insights, 1):
    with open(f"eda-in-{i}.txt", "w") as file:
        file.write(insight)
print("Exploratory data analysis completed. Insights saved to text files.")
next_script = "vis.py"
cmd = f"python3 {next_script} {file_path}"
os.system(cmd)