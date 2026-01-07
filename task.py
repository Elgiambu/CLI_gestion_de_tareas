import sys

comand_with_txt = {"add"}
comand_with_id_and_txt = {"done"}

class Task:
    def __init__(self):
        self.tasks = {}
        self.ids = {}
        self.last_task = ()
        self.comands = {"add": Task.add,
                        "ls" : Task.ls,
                        "quit": Task.quit,
                        "done": Task.done,
                        "remove": Task.remove}
        return

    def add(self,name):

        new_id = len(self.tasks) +1
        new_id = str(new_id)

        self.tasks[new_id] = [name,"Incomplete"]
        self.ids[name] = new_id
        self.last_task = (name, new_id)
        
        Task.fetch(self)

    def ls(self,name = None):
        if name == "milton":
            return print("NAAA MILTON PELOTUDO!!!!!!")

        if len(self.tasks) == 0:
            print("No added tasks")
        
        for task in self.tasks:
            task_name = self.tasks[task][0]
            task_state = self.tasks[task][1]
            print(f"task: {task_name}, id: {task}. {task_state}")
        
        Task.fetch(self)

    def done(self,reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        self.tasks[reference][1] = "done"

        Task.fetch(self)

    def remove(self,reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        self.tasks.pop(reference)        

    def execute_comand(self,cmd,name = None):
        
        if cmd in self.comands.keys():
            self.comands[cmd](self,name)
        
        else:
            return print("Command not valid")
        
    def quit(self,name = None):
        return
    
    def fetch(self):
        cmd = input("'quit' to close the program:  ")

        if cmd in comand_with_txt:
            name = input("task:  ")
            Task.execute_comand(self,cmd,name)
        
        else:
            Task.execute_comand(self,cmd)

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
        task = Task()
        task.execute_comand(cmd)

if __name__ == "__main__":
    main()