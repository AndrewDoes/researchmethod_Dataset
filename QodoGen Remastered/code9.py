
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.priorities = []

    def start(self):
        print("Welcome to the Task Scheduler!")
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

    def add_task(self):
        task_name = input("Enter task name: ")
        task_priority = input("Enter priority (High, Medium, Low): ")
        if task_priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Defaulting to Medium.")
            task_priority = "Medium"
        self.tasks.append(task_name)
        self.priorities.append(task_priority)
        print(f"Task '{task_name}' added with priority {task_priority}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for i, (task, priority) in enumerate(zip(self.tasks, self.priorities), start=1):
            print(f"{i}. {task} - Priority: {priority}")

    def complete_task(self):
        if not self.tasks:
            print("No tasks to complete.")
            return
        task_number = self.get_task_number("complete")
        if task_number is not None:
            index = task_number - 1
            print(f"Task '{self.tasks[index]}' marked as complete.")
            self.tasks.pop(index)
            self.priorities.pop(index)

    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
            return
        task_number = self.get_task_number("remove")
        if task_number is not None:
            index = task_number - 1
            print(f"Task '{self.tasks[index]}' removed.")
            self.tasks.pop(index)
            self.priorities.pop(index)

    def get_task_number(self, action):
        task_number = input(f"Enter task number to {action}: ")
        if not task_number.isdigit() or int(task_number) < 1 or int(task_number) > len(self.tasks):
            print("Invalid task number!")
            return None
        return int(task_number)

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.start()
