
import time
import random

class Task:
    PRIORITY_MAP = {1: "Low", 2: "Medium", 3: "High"}

    def __init__(self, title, description, due_days, priority=1):
        self.title = title
        self.description = description
        self.due_days = due_days
        self.status = "pending"
        self.priority = priority
        self.logs = []
        self.start_time = None
        self.end_time = None
        self.tags = []

    def start(self):
        self.start_time = time.time()
        self.log_activity("Task started")

    def stop(self):
        self.end_time = time.time()
        self.log_activity("Task stopped")

    def log_activity(self, message):
        self.logs.append(message)

    def calculate_duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0

    def update_status(self, status):
        self.status = status
        self.log_activity(f"Status updated to {status}")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due in: {self.due_days} days")
        print(f"Priority: {self.get_priority_value()}")
        print(f"Status: {self.status}")

    def print_logs(self):
        print("\n--- Task Logs ---")
        for log in self.logs:
            print(log)

    def delay_due(self, days):
        self.due_days += days

    def get_priority_value(self):
        return self.PRIORITY_MAP.get(self.priority, "Unknown")

    def add_random_tag(self):
        tags = ["urgent", "review", "optional", "bug"]
        self.tags.append(random.choice(tags))


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, due_days, priority=1):
        task = Task(title, description, due_days, priority)
        self.tasks.append(task)

    def show_tasks(self):
        print("\n--- Task List ---")
        for task in self.tasks:
            task.display_info()
            print("---")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def remove_task_by_title(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def count_completed_tasks(self):
        return sum(1 for task in self.tasks if task.status == "completed")

    def auto_complete_low_priority_tasks(self):
        for task in self.tasks:
            if task.priority == 1:
                task.update_status("completed")

    def find_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def export_task_titles(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(task.title + "\n")

    def add_random_tags_to_all_tasks(self):
        for task in self.tasks:
            task.add_random_tag()


def main():
    manager = TaskManager()
    manager.create_task("Fix login", "Users can’t log in after update", 3, 2)
    manager.create_task("Update docs", "Add API usage examples", 5, 1)
    manager.create_task("Deploy new build", "Push version 2.1", 2, 3)

    manager.show_tasks()
    task = manager.tasks[0]
    task.start()
    time.sleep(0.1)
    task.stop()
    task.print_logs()

    manager.auto_complete_low_priority_tasks()
    manager.export_task_titles()
    manager.add_random_tags_to_all_tasks()


if __name__ == "__main__":
    main()
