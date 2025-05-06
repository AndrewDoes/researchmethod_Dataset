
class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self) -> None:
        task_name = input("Enter task name: ")
        task_priority = input("Enter priority (High, Medium, Low): ")
        if task_priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Defaulting to Medium.")
            task_priority = "Medium"
        self.tasks.append({"name": task_name, "priority": task_priority})
        print(f"Task '{task_name}' added with priority {task_priority}.")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['name']} - Priority: {task['priority']}")

    def complete_task(self) -> None:
        if not self.tasks:
            print("No tasks to complete.")
            return
        task_number = self._get_task_number("Enter task number to mark as complete: ")
        if task_number is not None:
            task = self.tasks.pop(task_number)
            print(f"Task '{task['name']}' marked as complete.")

    def remove_task(self) -> None:
        if not self.tasks:
            print("No tasks to remove.")
            return
        task_number = self._get_task_number("Enter task number to remove: ")
        if task_number is not None:
            task = self.tasks.pop(task_number)
            print(f"Task '{task['name']}' removed.")

    def _get_task_number(self, prompt: str) -> int:
        task_number = input(prompt)
        if task_number.isdigit():
            index = int(task_number) - 1
            if 0 <= index < len(self.tasks):
                return index
        print("Invalid task number!")
        return None

    def menu(self) -> None:
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

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.menu()
