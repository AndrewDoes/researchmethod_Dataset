from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    priority: str = "Low"
    done: bool = False

class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self):
        desc = input("Enter task description: ")
        prio = input("Enter priority (High, Medium, Low): ")
        if prio not in ["High", "Medium", "Low"]:
            print("Invalid priority, defaulting to Low.")
            prio = "Low"
        self.tasks.append(Task(description=desc, priority=prio))
        print(f"Task '{desc}' added with priority {prio}.")

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
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(self.tasks):
                self.tasks[num-1].done = True
                print(f"Task '{self.tasks[num-1].description}' marked as done.")
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
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num-1)
                print(f"Task '{removed.description}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def start(self):
        print("Welcome to the Clean To-Do List!")
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

if __name__ == "__main__":
    ToDoList().start()