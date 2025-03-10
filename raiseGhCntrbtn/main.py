# Illegal tool to raise your contributions in GitHub
import os , time

repeat = int(input("How many contributions you want to add to ur account ? "))
path = input('Enter the path that you wanna push from it : ')
os.chdir(path)
with open('app.py','w') as file :
    while repeat != 0 :
        file.write('print("hello world")\n'*(repeat+1))
        repeat -=1
        os.system('git add .')
        commit = f'commit : {repeat}'
        time.sleep(3)
        os.system(f'git commit -m "commit : {commit}"')
        os.system("git push")
        print("done : ",repeat)
os.system("git push")