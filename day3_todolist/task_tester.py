from task_list import *

todo = TodoList()

todo.add_task("Buy milk")
todo.add_task("Walk dog")

print("== Initial Tasks ==")
todo.show_tasks()

todo.tasks[0].mark_completed()

print("\n== After Completing First Task ==")
todo.show_tasks()

todo.remove_task("Walk dog")

print("\n== After Removing Second Task ==")
todo.show_tasks()
