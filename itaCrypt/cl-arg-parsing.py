import sys,os
args = sys.argv

# functions we need :
letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]
def crypt(filename) :
    with open(filename,mode='r') as file :
        try :
            content = file.read()
            bc = '.'
            for i in content :
                        if ord(i) in list(range(65,90)) + list(range(97,122)) + list(range(48,75)) and i!="n" :
                            BinChar =  decimal_to_binary(ord(i))
                            bc += letters[int(BinChar[0:3],2)] + letters[int(BinChar[3:],2)] + '.'
                        elif i == "n" :
                              bc += i + '.'
                        else :
                            bc += i + '.'
            newFileName = filename[:filename.index('.')] + 'Encrypted' + filename[filename.index('.'):]
            open(newFileName,'w').write(bc)
            print("*** Conversion Completed ... (Result stored in: ",newFileName+") ***")
        except :
            print("*** FILE DOESN'T EXIST ... END PROCESSING *** \n")
def decrypt(filename) :
    try:
        with open(filename,mode='r') as file:
            content = file.read()
            OriginContent = ''
            i = 0
            while i < len(content):
                if i + 2 < len(content) and (content[i] in letters) and (content[i+1] in letters) and (content[i+2] == '.'):
                    left_bin = bin(letters.index(content[i]))[2:].zfill(3)
                    right_bin = bin(letters.index(content[i+1]))[2:].zfill(4)
                    ascii_binary = left_bin + right_bin
                    OriginContent += chr(int(ascii_binary, 2))
                    i += 3
                else:
                    OriginContent += content[i].replace('.','',1)
                    i += 1
            newFileName = filename[:filename.index('.')] + 'Decrypted' + filename[filename.index('.'):]
            open(newFileName,'w').write(OriginContent)
            print("*** Conversion Completed ... (Result stored in: ",newFileName+") ***")
    except :
            print("*** FILE DOESN'T EXIST ... END PROCESSING *** \n")
# running
if (len(args)!=3) or ('-' not in args[1])  :
    print("ERROR IN ARGUMENT SET")
else :
    mode = args[1]
    fileText = args[2]
    if mode == "-cf" :
        crypt(fileText)
    elif mode=="-df" :
        decrypt(fileText)
    elif mode == "-ct" :
        content = ''
        encryptedText = ''
        with open(fileText+'.txt',mode="w") as file :
            content = file.write(fileText)
        crypt(fileText+'.txt')
        with open(fileText+'Encrypted.txt',mode="r") as file :
            encryptedText = file.read()
        print(encryptedText)
        os.remove(fileText+'Encrypted.txt')
        os.remove(fileText+'.txt')
    elif mode == "-dt" :
        content = ''
        encryptedText = ''
        with open('dtClARGParsing.txt',mode="w") as file :
            content = file.write(fileText)
        decrypt('dtClARGParsing.txt')
        with open('dtClARGParsingDecrypted.txt',mode="r") as file :
            decryptedText = file.read()
        print(decryptedText)
        os.remove('dtClARGParsingDecrypted.txt')
        os.remove('dtClARGParsing.txt')
    else :
        print("ERROR IN ARGUMENT SET")

# Guide of how to use args :
    # cryptFile -> cf
    # cryptText -> ct
    # decryptFile -> df
    # decryptText -> dt