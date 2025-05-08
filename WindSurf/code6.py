class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_status = []
        self.priority = []

    def add_task(self) -> None:
        """Add a new task to the to-do list"""
        task = input("Enter task description: ")
        prio = input("Enter priority (High, Medium, Low): ")
        if prio not in ["High", "Medium", "Low"]:
            print("Invalid priority, defaulting to Low.")
            prio = "Low"
        self.tasks.append(task)
        self.task_status.append(False)
        self.priority.append(prio)
        print(f"Task '{task}' added with priority {prio}.")

    def view_tasks(self) -> None:
        """View all tasks in the to-do list"""
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for i in range(len(self.tasks)):
            status = "Done" if self.task_status[i] else "Not Done"
            print(f"{i+1}. {self.tasks[i]} - {status} - Priority: {self.priority[i]}")

    def mark_done(self) -> None:
        """Mark a task as done"""
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
            print("Invalid input. Please enter a number.")

    def remove_task(self) -> None:
        """Remove a task from the to-do list"""
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(self.tasks):
                del self.tasks[task_num]
                del self.task_status[task_num]
                del self.priority[task_num]
                print("Task removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def start_app() -> None:
    """Start the to-do list app"""
    print("Welcome to the Messy To-Do List!")
    todo_list = ToDoList()

    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.mark_done()
        elif choice == "4":
            todo_list.remove_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    start_app()