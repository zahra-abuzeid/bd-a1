import pandas as pd
import os
import sys
print("I AM IN DPRE")

# The dataset file path is provided as an argument by load.py
file_path = sys.argv[1]


df = pd.read_csv(file_path)


df.drop_duplicates(inplace=True)
df.drop(["notes", "name", "date_of_event", "date_of_death"], inplace=True, axis=1)

mean_age = df["age"].mean()
df["age"].fillna(mean_age, inplace=True)

for column in df.columns[8:14]:
    mode_value = df[column].mode().iloc[0]
    df[column].fillna(mode_value, inplace=True)

df.to_csv("res_dpre.csv", index=False)
print("Data preprocessing completed. res_dpre.csv created.")


next_script = "eda.py"
cmd = f"python3 {next_script} res_dpre.csv"
os.system(cmd)
