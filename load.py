import sys
import os
import pandas as pd
print("I AM IN LOAD")

if len(sys.argv) != 2:
    print("Usage: python3 load.py <dataset-path>")
else:
    file_path = sys.argv[1]

    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded :)) ")

        # Call the next script (dpre.py) and pass the dataset path as an argument
        cmd = f"python3 dpre.py {file_path}"
        os.system(cmd)

    except FileNotFoundError:
        print('File not found :( try again')
