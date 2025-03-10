# Illegal tool to raise your contributions in GitHub
import os , time

repeat = int(input("How many contributions you want to add to ur account ? "))
path = input('Enter the path that you wanna push from it : ')
os.chdir(path)

while repeat != 0 :
    with open('app.py','a') as file :
        file.write('print("hello world")\n')
    os.system(f'git commit -a -m "commit : {repeat}"')
    os.system("git push")
    print("done : ",repeat)
    repeat -=1

os.remove("app.py")
os.system('git commit -a -m "Ending inflating :)"')
os.system("git push")