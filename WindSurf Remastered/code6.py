# WindSurf Remastered/code6.py

# Data Structures
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

# Global Variables
tasks = []

# Functions
def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority level (high, medium, low): ")
    task = Task(name, priority)
    tasks.append(task)
    print(f"Task '{name}' added with priority {priority}.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task.done else "Not Done"
        print(f"{i}. {task.name} - {status} - Priority: {task.priority}")

def mark_task_done():
    if not tasks:
        print("No tasks available.")
        return
    view_tasks()
    task_number = int(input("Enter task number to mark as done: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task number.")
        return
    tasks[task_number].done = True
    print(f"Task '{tasks[task_number].name}' marked as done.")

def remove_task():
    if not tasks:
        print("No tasks available.")
        return
    view_tasks()
    task_number = int(input("Enter task number to remove: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task number.")
        return
    task_name = tasks.pop(task_number).name
    print(f"Task '{task_name}' removed.")

def start_app():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task Done\n4. Remove Task\n5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    start_app()