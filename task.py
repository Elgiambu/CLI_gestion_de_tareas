import sys

class Task:
    def __init__(self):
        self.tasks = {}
        self.last_task = ()
        self.comands = {"add": Task.add,
                        "ls" : Task.ls,
                        "salir": Task.salir}
        return

    def add(self):
        name = input("Por favor, ingresá la tarea:  ")
        new_id = len(self.tasks) +1

        self.tasks[new_id] = [name,"incomplete"]
        self.last_task = (name, id)
        
        print(f"nueva tarea agregada! : {name}, su id es {new_id}")
        Task.fetch(self)

    def fetch(self):
        cmd = input("Que necesitas? Para cerrar el programa ingresa el comando 'salir' :  ")
        Task.execute_comand(self,cmd)

    def ls(self):
        return

    def execute_comand(self,cmd):
        if cmd in self.comands.keys():
            self.comands[cmd](self)
        else: 
            print("comando no valido")

    def salir(self):
        return print("Hasta luego!")
    
def main():
    if len(sys.argv) > 2:
        print("Uso: python tasker.py <cmd>")
        return
    elif len(sys.argv) == 1:
        cmd = input("Que necesitas? Para cerrar el programa ingresa el comando 'salir' :  ")
    else:
        cmd = sys.argv[1]
    
    task = Task()
    task.execute_comand(cmd)

if __name__ == "__main__":
    main()