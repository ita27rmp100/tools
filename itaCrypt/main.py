# same encrypting system with python
letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]
fileName = input("Enter the file's name : ")
with open(fileName,'r') as file :
    try :
        content = file.read()
        bc = '.'
        for i in content :
            if ord(i) in list(range(65,90)) + list(range(97,122)) + list(range(48,75)) :
                BinChar =  decimal_to_binary(ord(i))
                bc += letters[int(BinChar[0:3],2)] + letters[int(BinChar[3:],2)] + '.'
            else :
                bc += i + '.'
        newFileName = fileName[:fileName.index('.')] + 'Encrypted' + fileName[fileName.index('.'):]
        open(newFileName,'w').write(bc)
        print("Conversion Completed ... (Result stored in: ",newFileName+")")
    except :
        print("FILE DOESN'T EXIST ... END PROCESSING\n")