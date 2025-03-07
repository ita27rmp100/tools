# same encrypting system with python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def decimal_to_binary(n):
    return format(n, "07b")
with open('text.txt','r') as file :
    content = file.read()
    BinCONTENT = ''
    for i in content :
        if ord(i) in list(range(65,90)) + list(range(97,122)) + list(range(48,75)) :
            BinCONTENT += str(decimal_to_binary(ord(i))) + ' '
            # BinChar = 
        else :
            BinCONTENT += i
print(BinCONTENT)
print("completed")