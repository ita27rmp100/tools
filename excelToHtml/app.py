from PyCSV import main
import pandas as pd

# import file.excel and convert it to file.csv
df = pd.read_excel("file.xlsx")
print(df)