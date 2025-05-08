class ToDoListApp:
    def __init__(self):
        self.tasks = []
        self.priorities = []

    def start(self) -> None:
        """Start the to-do list app"""
        print("Welcome to the To-Do List App!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.remove_task()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self) -> None:
        """Display the main menu"""
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Quit")

    def add_task(self) -> None:
        """Add a new task to the list"""
        task_name = input("Enter task name: ")
        task_priority = input("Enter priority (High, Medium, Low): ")
        if task_priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Defaulting to Medium.")
            task_priority = "Medium"
        self.tasks.append(task_name)
        self.priorities.append(task_priority)
        print(f"Task '{task_name}' added with priority {task_priority}.")

    def view_tasks(self) -> None:
        """View all tasks in the list"""
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- Task List ---")
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i]} - Priority: {self.priorities[i]}")

    def complete_task(self) -> None:
        """Complete a task"""
        if not self.tasks:
            print("No tasks to complete.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to complete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                print(f"Task '{self.tasks[task_num]}' completed!")
                del self.tasks[task_num]
                del self.priorities[task_num]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_task(self) -> None:
        """Remove a task from the list"""
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(self.tasks):
                print(f"Task '{self.tasks[task_num]}' removed!")
                del self.tasks[task_num]
                del self.priorities[task_num]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:
    app = ToDoListApp()
    app.start()

if __name__ == "__main__":
    main()