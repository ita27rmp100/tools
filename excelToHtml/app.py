from PyCSV import main
import pandas as pd

# import file.excel and convert it to file.csv
df = main.data("file.csv")
print(df)