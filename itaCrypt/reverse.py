letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]
fileName = input("Enter the encrypted file name : ")
with open(fileName,'r') as file :
    try :
        content = file.read()
        bc = ''
        i = 1
        while i != len(content) :
            step = content[i:content.index('.')-1]
            if (len(step) == 2) and (step[0] and step[0] in letters) :
                pass
        print("Conversion Completed ... (Result stored in: ",newFileName+")")
    except :
        print("FILE DOESN'T EXIST ... END PROCESSING\n")