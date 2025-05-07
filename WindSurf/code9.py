# WindSurf/code9.py

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Enter task description: ")
        priority = input("Enter priority (High, Medium, Low): ")
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority, defaulting to Low.")
            priority = "Low"
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- Task List ---")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.description} - Priority: {task.priority}")

    def complete_task(self):
        if not self.tasks:
            print("No tasks to complete.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to complete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                completed_task = self.tasks.pop(task_num)
                print(f"Task '{completed_task.description}' completed successfully.")
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
                print(f"Task '{removed_task.description}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def menu():
    task_manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.complete_task()
        elif choice == "4":
            task_manager.remove_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()