# same encrypting system with python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def decimal_to_binary(n):
    return f"{n:07b}"
with open('text.txt','r') as file :
    content = file.read()
    BinCONTENT = ''
    for i in content :
        if i in letters :
            if i in letters[0:25] :
                BinChar = letters.index(i) + 65
            elif i in letters[26:51] :
                BinChar = letters.index(i) + 97
            else :
                BinChar = letters.index(i) + 48
            BinChar = decimal_to_binary(BinChar)
            print(BinChar)
            BinCONTENT += str(BinChar) + ' '
            BinChar = 
        else :
            BinCONTENT += i
print(BinCONTENT)
print("completed")