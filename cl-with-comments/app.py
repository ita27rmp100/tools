import sys , os , sqlite3
from tabulate import tabulate
from termcolor import colored
# Create a connection to the SQLite database
connection = sqlite3.connect('history.db')
cursor = connection.cursor()
# colored print :
def printf(msg,color) :
    print(colored("$cl-with-cmnts -> " + msg,color))
# create table history
try :
    cursor.execute('create table history (command varchar(255), comment varchar(100))')
except sqlite3.OperationalError:
    pass
# execute the command line arguments
args = sys.argv
args.pop(0) 
if len(args) == 0:
    printf("No arguments provided.", 'red')
elif len(args) == 1 :
    if args[0] == 'dh':
        cursor.execute('select * from history')
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        print(tabulate(data,headers=column_names,tablefmt='grid'))
    elif args[0] == "cls" :
        cursor.execute("delete from history")
        data = cursor.fetchall()
        connection.commit()
        printf("History cleared.","green")
    else :
        os.system(args[0])
        cursor.execute("insert into history values(?,?)", (args[0], ' '))
        connection.commit()
        printf("Command executed and logged.","green")
        cursor.execute('select * from history')
elif len(args) ==2 or len(args)==1 :
    os.system(args[0])
    cursor.execute("insert into history values(?,?)", (args[0], args[1] or ' '))
    connection.commit()
    printf("Command executed and logged.","green")
    cursor.execute('select * from history')
else :
    printf("Invalid number of arguments. Please provide a command and a comment.","red")
cursor.close()