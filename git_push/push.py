import os
os.chdir(input('Enter the work directory you wanna push it : '))
os.system("git add .")
commit = input("Enter commit message : ")
os.system(f'git commit -m "{commit}"')
os.system('git push')