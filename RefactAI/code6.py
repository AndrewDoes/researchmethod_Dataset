from typing import List

class Task:
    def __init__(self, description: str, priority: str):
        self.description = description
        self.priority = priority if priority in ["High", "Medium", "Low"] else "Low"
        self.done = False

    def __str__(self):
        status = "Done" if self.done else "Not Done"
        return f"{self.description} - {status} - Priority: {self.priority}"

class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self):
        description = input("Enter task description: ")
        prio = input("Enter priority (High, Medium, Low): ")
        if prio not in ["High", "Medium", "Low"]:
            print("Invalid priority, defaulting to Low.")
            prio = "Low"
        self.tasks.append(Task(description, prio))
        print(f"Task '{description}' added with priority {prio}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_done(self):
        if not self.tasks:
            print("No tasks to mark.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num].done = True
                print(f"Task '{self.tasks[task_num].description}' marked as done.")
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
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                print(f"Task '{removed_task.description}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def start_app(self):
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
    todo = ToDoList()
    todo.start_app()