import time
import random
from enum import Enum, auto
from typing import List, Optional

class Status(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    @classmethod
    def from_value(cls, value):
        for p in cls:
            if p.value == value:
                return p
        return None

class Task:
    def __init__(self, title: str, desc: str, due: int, 
                 status: Status = Status.PENDING, 
                 priority: Priority = Priority.LOW):
        self.title = title
        self.desc = desc
        self.due = due
        self.status = status
        self.priority = priority
        self.logs: List[str] = []
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.tags: List[str] = []

    def start(self):
        self.start_time = time.time()
        self.logs.append("Task started")

    def stop(self):
        self.end_time = time.time()
        self.logs.append("Task stopped")

    def log_activity(self, msg: str):
        self.logs.append(msg)

    def calculate_duration(self) -> Optional[float]:
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return None

    def update_status(self, status: Status):
        self.status = status
        if status == Status.COMPLETED:
            self.logs.append("Completed")
        elif status == Status.CANCELLED:
            self.logs.append("Cancelled")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.desc}")
        print(f"Due: {self.due}")
        print(f"Priority: {self.priority.name}")
        print(f"Status: {self.status.value}")

    def print_logs(self):
        for log in self.logs:
            print(log)

    def delay_due(self, days: int):
        self.due += days

    def get_priority_label(self) -> str:
        return self.priority.name.capitalize()

class TaskManager:
    def __init__(self):
        self.task_list: List[Task] = []
        self.last_task: Optional[Task] = None

    def create_task(self, title: str, desc: str, due: int, priority: int = 1):
        prio = Priority.from_value(priority) or Priority.LOW
        task = Task(title, desc, due, priority=prio)
        self.task_list.append(task)
        self.last_task = task

    def show_tasks(self):
        for t in self.task_list:
            t.display_info()
            print("---")

    def remove_task(self, task: Task):
        if task in self.task_list:
            self.task_list.remove(task)

    def remove_task_by_title(self, title: str):
        self.task_list = [t for t in self.task_list if t.title != title]

    def count_completed(self) -> int:
        return sum(1 for t in self.task_list if t.status == Status.COMPLETED)

    def auto_complete_low_priority(self):
        for t in self.task_list:
            if t.priority == Priority.LOW:
                t.update_status(Status.COMPLETED)

    def find_by_priority(self, priority: int) -> List[Task]:
        prio = Priority.from_value(priority)
        return [t for t in self.task_list if t.priority == prio]

    def export_task_titles(self, filename: str = "tasks.txt"):
        with open(filename, "w") as f:
            for t in self.task_list:
                f.write(t.title + "\n")

    def add_random_tag_to_all(self):
        tags = ["urgent", "review", "optional", "bug"]
        for t in self.task_list:
            t.tags.append(random.choice(tags))

# Main flow
if __name__ == "__main__":
    mgr = TaskManager()
    mgr.create_task("Fix login", "Users can’t log in after update", 3, 2)
    mgr.create_task("Update docs", "Add API usage examples", 5, 1)
    mgr.create_task("Deploy new build", "Push version 2.1", 2, 3)

    mgr.show_tasks()
    mgr.task_list[0].start()
    time.sleep(0.1)
    mgr.task_list[0].stop()
    mgr.task_list[0].print_logs()

    mgr.auto_complete_low_priority()
    mgr.export_task_titles()
    mgr.add_random_tag_to_all()