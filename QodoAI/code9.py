class Task:
    def __init__(self, name: str, priority: str = "Medium") -> None:
        self.name = name
        self.priority = priority if priority in ["High", "Medium", "Low"] else "Medium"

    def __str__(self) -> str:
        return f"{self.name} - Priority: {self.priority}"


class TaskScheduler:
    def __init__(self) -> None:
        self.tasks = []

    def menu(self) -> None:
        actions = {
            "1": self.add_task,
            "2": self.view_tasks,
            "3": self.complete_task,
            "4": self.remove_task,
        }
        while True:
            print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
            option = input("Choose an option: ")
            if option in actions:
                actions[option]()
            elif option == "5":
                print("Exiting Task Scheduler...")
                break
            else:
                print("Invalid choice! Try again.")

    def add_task(self) -> None:
        name = input("Enter task name: ")
        priority = input("Enter priority (High, Medium, Low): ")
        task = Task(name, priority)
        self.tasks.append(task)
        print(f"Task '{task.name}' added with priority {task.priority}.")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self) -> None:
        if not self.tasks:
            print("No tasks to complete.")
            return
        task_number = self._get_task_number("Enter task number to mark as complete: ")
        if task_number is not None:
            print(f"Task '{self.tasks[task_number].name}' marked as complete.")
            self.tasks.pop(task_number)

    def remove_task(self) -> None:
        if not self.tasks:
            print("No tasks to remove.")
            return
        task_number = self._get_task_number("Enter task number to remove: ")
        if task_number is not None:
            print(f"Task '{self.tasks[task_number].name}' removed.")
            self.tasks.pop(task_number)

    def _get_task_number(self, prompt: str) -> int:
        try:
            task_number = int(input(prompt)) - 1
            if 0 <= task_number < len(self.tasks):
                return task_number
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")
        return None


if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.menu()