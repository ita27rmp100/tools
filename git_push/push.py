# import os
# os.chdir(input('Enter the work directory you wanna push it : '))
# os.system("git add .")
# commit = input("Enter commit message : ")
# os.system(f"git commit -m '{commit}'")
# os.system('git push')
import os

# Change directory
os.chdir(input('Enter the work directory you wanna push it : '))

# Stage changes
os.system("git add .")

# Get commit message and handle single quotes
commit = input("Enter commit message : ")
commit = commit.replace("'", r"'\''")  # Escape single quotes if they exist

# Commit changes
os.system(f'git commit -m "{commit}"')

# Push changes
os.system('git push')
