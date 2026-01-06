import sys

comandos = ["add"]

class Task:
    def __init__(self):
        self.tasks = []

    def add(self, new_task):
        self.tasks.append(new_task)
        print(f"nueva tarea agregada: {new_task}")

    def execute_comand(self,cmd,txt):
        if hasattr(self,cmd):
            getattr(self,cmd)(txt)
        else:
            print("comando no valido")

def main():
    if len(sys.argv) < 3:
        print("Uso: python tasker.py <comando> <texto>")
        
        return
    
    cmd = sys.argv
    txt = sys.argv
    
    task = Task()
    task.execute_comand(cmd,txt)

if __name__ == "__main__":
    main()