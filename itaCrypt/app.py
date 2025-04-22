nameTool = """
#  .▄▄▄▄▄▄▄▄▄▄▄..▄▄▄▄▄▄▄▄▄▄▄..▄▄▄▄▄▄▄▄▄▄▄..▄▄▄▄▄▄▄▄▄▄▄..▄▄▄▄▄▄▄▄▄▄▄..▄.........▄..▄▄▄▄▄▄▄▄▄▄▄..▄▄▄▄▄▄▄▄▄▄▄.
#  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌.......▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  .▀▀▀▀█░█▀▀▀▀..▀▀▀▀█░█▀▀▀▀.▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀.▐░█▀▀▀▀▀▀▀█░▌▐░▌.......▐░▌▐░█▀▀▀▀▀▀▀█░▌.▀▀▀▀█░█▀▀▀▀.
#  .....▐░▌..........▐░▌.....▐░▌.......▐░▌▐░▌..........▐░▌.......▐░▌▐░▌.......▐░▌▐░▌.......▐░▌.....▐░▌.....
#  .....▐░▌..........▐░▌.....▐░█▄▄▄▄▄▄▄█░▌▐░▌..........▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌.....▐░▌.....
#  .....▐░▌..........▐░▌.....▐░░░░░░░░░░░▌▐░▌..........▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌.....▐░▌.....
#  .....▐░▌..........▐░▌.....▐░█▀▀▀▀▀▀▀█░▌▐░▌..........▐░█▀▀▀▀█░█▀▀..▀▀▀▀█░█▀▀▀▀.▐░█▀▀▀▀▀▀▀▀▀......▐░▌.....
#  .....▐░▌..........▐░▌.....▐░▌.......▐░▌▐░▌..........▐░▌.....▐░▌.......▐░▌.....▐░▌...............▐░▌.....
#  .▄▄▄▄█░█▄▄▄▄......▐░▌.....▐░▌.......▐░▌▐░█▄▄▄▄▄▄▄▄▄.▐░▌......▐░▌......▐░▌.....▐░▌...............▐░▌.....
#  ▐░░░░░░░░░░░▌.....▐░▌.....▐░▌.......▐░▌▐░░░░░░░░░░░▌▐░▌.......▐░▌.....▐░▌.....▐░▌...............▐░▌.....
#  .▀▀▀▀▀▀▀▀▀▀▀.......▀.......▀.........▀..▀▀▀▀▀▀▀▀▀▀▀..▀.........▀.......▀.......▀.................▀......
#  ........................................................................................................
"""
letters = "$^#*|!~?/%&=+-~@"
decimal_to_binary = lambda n: bin(n)[2:]

print(nameTool)
while True :
    option = int(input("$ Select option 0 if encypt , 1 if decrypt , 2 to stop : "))
    if option == 2 :
            print("***GOODBYE BRO***")
            break
    try:
        fileName = input("$ Enter the file's name : ")
        if option == 0 :
            with open(fileName,'r') as file :
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
                    newFileName = fileName[:fileName.index('.')] + 'Encrypted' + fileName[fileName.index('.'):]
                    open(newFileName,'w').write(bc)
                    print("*** Conversion Completed ... (Result stored in: ",newFileName+") ***")
                except :
                    print("*** FILE DOESN'T EXIST ... END PROCESSING *** \n")
        elif option == 1 :
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
        else :
            print("OPTION IS NOT VALID")
    except NameError as msg:
        print(msg)