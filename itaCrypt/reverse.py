letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]
fileName = input("Enter the encrypted file name : ")
with open(fileName,'r') as file :
    try :
        content = file.read()
        OriginContent = ''
        i = 1
        while i <= len(content) :
            step = content[i:content.index('.')-1]
            if (len(step) == 2) and (step[0] and step[1] in letters) :
                ascii = (bin(letters.index(step[0]))[2:]).zfill(3) + (bin(letters.index(step[0]))[2:]).zfill(4)
                OriginContent += ascii
            i += 1
        print(OriginContent)
    except :
        print("FILE DOESN'T EXIST ... END PROCESSING\n")