# Illegal tool to raise your contributions in GitHub
import os

repeat = input("How many contributions you want to add to ur account ? ")
with open('appp.py','a') as file :
    while repeat != 0 :
        file.write(f'print({repeat})')
        repeat -=1
        os.system('git add .')
        os.system(f"git commit -m 'commit : {abs(0-repeat)}'")
        os.system('git push')
        print("done : ",repeat)