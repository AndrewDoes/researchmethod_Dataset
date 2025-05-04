class Task:
    def __init__(self, description: str, priority: str = "Low") -> None:
        self.description = description
        self.priority = priority if priority in ["High", "Medium", "Low"] else "Low"
        self.is_done = False

    def mark_done(self) -> None:
        self.is_done = True

    def __str__(self) -> str:
        status = "Done" if self.is_done else "Not Done"
        return f"{self.description} - {status} - Priority: {self.priority}"


class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self) -> None:
        description = input("Enter task description: ")
        priority = input("Enter priority (High, Medium, Low): ")
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task '{description}' added with priority {task.priority}.")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_task_done(self) -> None:
        if not self.tasks:
            print("No tasks to mark.")
            return
        self.view_tasks()
        task_num = self._get_task_number("Enter task number to mark as done: ")
        if task_num is not None:
            self.tasks[task_num].mark_done()
            print(f"Task '{self.tasks[task_num].description}' marked as done.")

    def remove_task(self) -> None:
        if not self.tasks:
            print("No tasks to remove.")
            return
        self.view_tasks()
        task_num = self._get_task_number("Enter task number to remove: ")
        if task_num is not None:
            removed_task = self.tasks.pop(task_num)
            print(f"Task '{removed_task.description}' removed.")

    def _get_task_number(self, prompt: str) -> int:
        try:
            task_num = int(input(prompt)) - 1
            if 0 <= task_num < len(self.tasks):
                return task_num
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        return None


def start_app() -> None:
    print("Welcome to the Refactored To-Do List!")
    todo_list = ToDoList()
    actions = {
        "1": todo_list.add_task,
        "2": todo_list.view_tasks,
        "3": todo_list.mark_task_done,
        "4": todo_list.remove_task,
    }
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Remove Task\n5. Quit")
        choice = input("Enter choice: ")
        if choice in actions:
            actions[choice]()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    start_app()