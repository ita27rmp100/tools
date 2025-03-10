def data(fc) :
    with open(fc) as file :
        return file.read().splitlines()
def dataMatrix(fc) :
    DATA = data(fc)
    for i in range(0,len(DATA)) :
        DATA[i] = str(DATA[i]).split(',')
    return DATA
def data_Vr(fc) : 
    DATA = dataMatrix(fc)
    vertical = {}
    for i in range(0,len(DATA[0])) :
        vertical[DATA[0][i]] = []
        for j in range(1,len(DATA)) :
            vertical[DATA[0][i]].append(DATA[j][i])
    return vertical
def number_of(fc,mode="c") : # Counts the number of columns, rows and cells in a CSV file
    rows = len(data(fc))
    columns = data_Vr(fc).keys().__len__()
    if mode == "ce" : #counts number of cells
        return rows*columns
    elif  mode[0] == "r" : #counts rows number
        return rows
    elif mode == "co" : #counts columns number
        return columns
def csv_files_in(folder) :  # return the csv files in folder 
    import os
    csvFiles = []
    for i in os.listdir(r"{}".format(folder)) :
        if i[-4:] == ".csv" :
            csvFiles.append(i)
    return csvFiles
def creat_and_write(fc,data="\n") : # create csv file and write  in it
    with open(r"{}".format(fc),mode="a") as file :
        file.write(data)
    return "created"
def read(fc) :
    with open(fc) as file :
        return file.read()
def keyword(fc,word) : #receive a keyword and then search for the row it belongs to
    DATA = data(fc)
    for i in DATA :
        if word in i :
            return i 
def index_cell(fc,cellContent) : #return the place of cell in the file
    d = data(fc)
    z = str(keyword(fc,cellContent))
    y = d.index(z)+1
    x = z[0:z.index(cellContent)].count(";")+1
    return {"x":x,"y":y}
def clear(fc) : #delete data in file csv
    with open(fc,mode="w") as file :
        pass
def CSVtoXLSX(fc): #create a copy with .xlsx extension
    import pandas as pd
    df = pd.read_csv(fc)
    excel_filename = f"{fc[:-4]}.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Successfully converted '{fc}' to '{excel_filename}'")