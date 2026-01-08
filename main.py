import sys
from task import Task
from tasks import Tasks

def main():
    
    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Use: python tasker.py <cmd> <name_task>")
        return
    
    elif len(sys.argv) == 3:
        cmd = sys.argv[1]
        name = sys.argv[2]

        task = Task()  
        task.execute_comand(cmd,name)
    
    else:
        cmd = input("'quit' to close the program:  ")

    if cmd in comand_with_txt:
        name = input("task:  ")
        task = Task()  
        task.execute_comand(cmd,name)
    elif cmd in comand_with_id_and_txt:
        name = input("task or id:  ")
    else:
        task = Tasks()
        task.execute_comand(cmd)

if __name__ == "__main__":
    main()