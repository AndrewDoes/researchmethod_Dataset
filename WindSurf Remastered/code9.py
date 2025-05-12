# WindSurf Remastered/code9.py

# Constants
PRIORITY_LEVELS = ["High", "Medium", "Low"]
OPTIONS = {
    "1": "Add Task",
    "2": "View Tasks",
    "3": "Complete Task",
    "4": "Remove Task",
    "5": "Exit"
}

# Data Structures
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        """Add a new task to the list"""
        task_name = input("Enter task name: ")
        task_priority = self.get_task_priority()
        self.tasks.append(Task(task_name, task_priority))
        print(f"Task '{task_name}' added with priority {task_priority}.")

    def view_tasks(self):
        """Display all tasks in the list"""
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.name} - Priority: {task.priority}")

    def complete_task(self):
        """Mark a task as complete"""
        if not self.tasks:
            print("No tasks to complete.")
            return
        task_number = self.get_task_number()
        if task_number:
            print(f"Task '{self.tasks[task_number-1].name}' marked as complete.")
            self.tasks.pop(task_number-1)

    def remove_task(self):
        """Remove a task from the list"""
        if not self.tasks:
            print("No tasks to remove.")
            return
        task_number = self.get_task_number()
        if task_number:
            print(f"Task '{self.tasks[task_number-1].name}' removed.")
            self.tasks.pop(task_number-1)

    def get_task_priority(self):
        """Get task priority from user input"""
        while True:
            priority = input("Enter priority (High, Medium, Low): ")
            if priority in PRIORITY_LEVELS:
                return priority
            print("Invalid priority! Please choose from High, Medium, or Low.")

    def get_task_number(self):
        """Get task number from user input"""
        while True:
            try:
                task_number = int(input("Enter task number: "))
                if 1 <= task_number <= len(self.tasks):
                    return task_number
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def display_menu(self):
        """Display the main menu"""
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")

    def run(self):
        """Run the task manager"""
        while True:
            self.display_menu()
            option = input("Choose an option: ")
            if option == "1":
                self.add_task()
            elif option == "2":
                self.view_tasks()
            elif option == "3":
                self.complete_task()
            elif option == "4":
                self.remove_task()
            elif option == "5":
                break
            else:
                print("Invalid option! Please choose a valid option.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()