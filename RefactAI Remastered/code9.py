from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str = "Medium"

class TaskScheduler:
    PRIORITIES = ["High", "Medium", "Low"]

    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_name = input("Enter task name: ")
        task_priority = input("Enter priority (High, Medium, Low): ")
        if task_priority not in self.PRIORITIES:
            print("Invalid priority! Defaulting to Medium.")
            task_priority = "Medium"
        self.tasks.append(Task(task_name, task_priority))
        print(f"Task '{task_name}' added with priority {task_priority}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task.name} - Priority: {task.priority}")

    def complete_task(self):
        if not self.tasks:
            print("No tasks to complete.")
            return
        self.view_tasks()
        task_number = input("Enter task number to mark as complete: ")
        if not task_number.isdigit() or not (1 <= int(task_number) <= len(self.tasks)):
            print("Invalid task number!")
            return
        index = int(task_number) - 1
        print(f"Task '{self.tasks[index].name}' marked as complete.")
        self.tasks.pop(index)

    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        task_number = input("Enter task number to remove: ")
        if not task_number.isdigit() or not (1 <= int(task_number) <= len(self.tasks)):
            print("Invalid task number!")
            return
        index = int(task_number) - 1
        print(f"Task '{self.tasks[index].name}' removed.")
        self.tasks.pop(index)

    def menu(self):
        while True:
            print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
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
                print("Exiting Task Scheduler...")
                break
            else:
                print("Invalid choice! Try again.")

def main():
    scheduler = TaskScheduler()
    scheduler.menu()

if __name__ == "__main__":
    main()