from dataclasses import dataclass, field

@dataclass
class Task:
    description: str
    priority: str = "Low"
    done: bool = False

class ToDoList:
    PRIORITIES = ["High", "Medium", "Low"]

    def __init__(self):
        self.tasks = []

    def start_app(self):
        print("Welcome to the Messy To-Do List!")
        while True:
            print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Remove Task\n5. Quit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_done()
            elif choice == "4":
                self.remove_task()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

    def add_task(self):
        task_desc = input("Enter task description: ")
        prio = input("Enter priority (High, Medium, Low): ")
        if prio not in self.PRIORITIES:
            print("Invalid priority, defaulting to Low.")
            prio = "Low"
        self.tasks.append(Task(description=task_desc, priority=prio))
        print(f"Task '{task_desc}' added with priority {prio}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task.done else "Not Done"
            print(f"{idx}. {task.description} - {status} - Priority: {task.priority}")

    def mark_done(self):
        if not self.tasks:
            print("No tasks to mark.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1].done = True
                print(f"Task '{self.tasks[task_num - 1].description}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)
                print(f"Task '{removed_task.description}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo = ToDoList()
    todo.start_app()

if __name__ == "__main__":
    main()