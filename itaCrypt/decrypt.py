letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]
fileName = input("$ Enter the encrypted file name : ")
try:
    with open(fileName, 'r') as file:
        content = file.read()
    OriginContent = ''
    i = 0
    while i < len(content):
        if i + 2 < len(content) and content[i] in letters and content[i+1] in letters and content[i+2] == '.':
            left_bin = bin(letters.index(content[i]))[2:].zfill(3)
            right_bin = bin(letters.index(content[i+1]))[2:].zfill(4)
            ascii_binary = left_bin + right_bin
            OriginContent += chr(int(ascii_binary, 2))
            i += 3  # Skip the two-letter token and the dot.
        else:
            OriginContent += content[i].replace('.','',1)
            i += 1
    newFileName = fileName[:fileName.index('.')] + 'Decrypted' + fileName[fileName.index('.'):]
    open(newFileName,'w').write(OriginContent)
    print("*** Conversion Completed ... (Result stored in: ",newFileName+") ***")
except :
        print("*** FILE DOESN'T EXIST ... END PROCESSING *** \n")