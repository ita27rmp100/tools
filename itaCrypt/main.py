# same encrypting system with python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def decimal_to_binary(n):
    return format(n, "07b")
fileName = input("Enter the file's name :")
with open(fileName,'r') as file :
    try :
        content = file.read()
        BinCONTENT = ''
        bc = ''
        for i in content :
            if ord(i) in list(range(65,90)) + list(range(97,122)) + list(range(48,75)) :
                BinCONTENT += str(decimal_to_binary(ord(i))) + ' '
                BinChar =  decimal_to_binary(ord(i))
                BinChar = int(BinChar[0:3],2) + int(BinChar[3:],2)
                bc += letters[BinChar]
                # BinChar = 
            else :
                BinCONTENT += i
                bc += i
        newFileName = fileName[:fileName.index('.')] + 'Encrypted' + fileName[fileName.index('.'):]
        open(newFileName,'w').write(bc)
        print("Conversion Completed ... (Result stored in: ",newFileName+")")
    except :
        print("FILE DOESN'T EXIST ... END PROCESSING\n")