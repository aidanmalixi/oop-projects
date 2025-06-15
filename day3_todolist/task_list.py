class Task:
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True


class TodoList:
    def __init__(self):
        self.tasks = []  

    def add_task(self, description):
        task = Task(description)       
        self.tasks.append(task)         

    def remove_task(self, description):

        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                break  

    def show_tasks(self):
        for index, task in enumerate(self.tasks, 1):  
            status = "complete" if task.is_completed else "not complete"
            print(f"{index}. {status} {task.description}")
