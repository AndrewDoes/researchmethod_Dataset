# WindSurf/code17.py

class Task:
    def __init__(self, title, desc, due, status="pending", priority=1):
        self.title = title
        self.desc = desc
        self.due = due
        self.status = status
        self.priority = priority
        self.logs = []
        self.start_time = None
        self.end_time = None
        self.tags = []

    def start(self):
        self.start_time = time.time()
        self.logs.append("Task started")

    def stop(self):
        self.end_time = time.time()
        self.logs.append("Task stopped")

    def __str__(self):
        return f"Title: {self.title}, Description: {self.desc}, Due: {self.due}, Status: {self.status}, Priority: {self.priority}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = self._get_task_details()
        self.tasks.append(task)
        print("Task Added!")

    def _get_task_details(self):
        title = input("Enter task title: ")
        desc = input("Enter task description: ")
        due = input("Enter task due date: ")
        priority = int(input("Enter task priority: "))

        return Task(title, desc, due, priority=priority)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- Task List ---")
        for task in self.tasks:
            print(task)

    def update_task(self):
        title = input("Enter task title to update: ")
        task = self._find_task(title)
        if task:
            task.title = input("Enter new title: ")
            task.desc = input("Enter new description: ")
            task.due = input("Enter new due date: ")
            task.priority = int(input("Enter new priority: "))
            print("Task Updated!")
        else:
            print("Task not found!")

    def _find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def delete_task(self):
        title = input("Enter task title to delete: ")
        self.tasks = [task for task in self.tasks if task.title != title]
        print("Task Deleted!")

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task\n2. Display Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.display_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()