class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_status = []
        self.priority = []

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
        task = input("Enter task description: ")
        prio = input("Enter priority (High, Medium, Low): ")
        if prio not in ["High", "Medium", "Low"]:
            print("Invalid priority, defaulting to Low.")
            prio = "Low"
        self.tasks.append(task)
        self.task_status.append(False)
        self.priority.append(prio)
        print(f"Task '{task}' added with priority {prio}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks):
            status = "Done" if self.task_status[i] else "Not Done"
            print(f"{i+1}. {task} - {status} - Priority: {self.priority[i]}")

    def mark_done(self):
        if not self.tasks:
            print("No tasks to mark.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.task_status[task_num] = True
                print(f"Task '{self.tasks[task_num]}' marked as done.")
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
                self.task_status.pop(task_num)
                self.priority.pop(task_num)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.start_app()
