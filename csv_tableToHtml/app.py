import PyCSV
# WELCOME TO SCRIPT & INPUT FILE NAME
fileName = input("Enter excel file (without .csv) : ")
# import file.eDATAcel and convert it to file.csv
try :
    data = PyCSV.dataMatrix(f"{fileName}.csv")
    htmlTable = '<table>\n'
    for i in data :
        row = " "*4 + '<tr>\n'
        for j in i :
            row += " "*8 + f"<td>{j}</td>\n"
        row += "    </tr>\n"  
        htmlTable += row
    htmlTable += "</table>"
    with open(f"{fileName}_TABLE.html",mode="w") as html :
        html.write(htmlTable)
    print("DONE ...")
except :
    print("ERROR, FILENAME DOESN'T EXIST OR CANNOT BE TREATED NOW")