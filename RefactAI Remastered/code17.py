import time
import random
from enum import Enum
from typing import List, Optional

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

PRIORITY_LABELS = {
    TaskPriority.LOW: "Low",
    TaskPriority.MEDIUM: "Medium",
    TaskPriority.HIGH: "High"
}

class Task:
    """
    Represents a single task with status, priority, logs, and timing.
    """
    def __init__(
        self, 
        title: str, 
        description: str, 
        due_in_days: int, 
        status: TaskStatus = TaskStatus.PENDING, 
        priority: TaskPriority = TaskPriority.LOW
    ):
        self.title = title
        self.description = description
        self.due_in_days = due_in_days
        self.status = status
        self.priority = priority
        self.logs: List[str] = []
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.tags: List[str] = []

    def start(self) -> None:
        """Mark the task as started and log the event."""
        self.start_time = time.time()
        self.log_activity("Task started")

    def stop(self) -> None:
        """Mark the task as stopped and log the event."""
        self.end_time = time.time()
        self.log_activity("Task stopped")

    def log_activity(self, message: str) -> None:
        """Add a log entry for the task."""
        self.logs.append(message)

    def calculate_duration(self) -> Optional[float]:
        """Calculate the duration between start and stop."""
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return None

    def update_status(self, new_status: TaskStatus) -> None:
        """Update the task status and log the change."""
        self.status = new_status
        status_logs = {
            TaskStatus.COMPLETED: "Completed",
            TaskStatus.CANCELLED: "Cancelled"
        }
        if new_status in status_logs:
            self.log_activity(status_logs[new_status])

    def display_info(self) -> None:
        """Print task details."""
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due in (days): {self.due_in_days}")
        print(f"Priority: {self.get_priority_label()}")
        print(f"Status: {self.status.value}")

    def print_logs(self) -> None:
        """Print all log entries for the task."""
        for log in self.logs:
            print(log)

    def delay_due(self, days: int) -> None:
        """Delay the due date by a number of days."""
        self.due_in_days += days

    def get_priority_label(self) -> str:
        """Return the string label for the task's priority."""
        return PRIORITY_LABELS.get(self.priority, "Unknown")

class TaskManager:
    """
    Manages a collection of Task objects.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.last_task: Optional[Task] = None

    def create_task(
        self, 
        title: str, 
        description: str, 
        due_in_days: int, 
        priority: TaskPriority = TaskPriority.LOW
    ) -> None:
        """Create and add a new task."""
        task = Task(title, description, due_in_days, priority=priority)
        self.tasks.append(task)
        self.last_task = task

    def show_tasks(self) -> None:
        """Display all tasks."""
        for task in self.tasks:
            task.display_info()
            print("---")

    def remove_task(self, task: Task) -> None:
        """Remove a task by object reference."""
        if task in self.tasks:
            self.tasks.remove(task)

    def remove_task_by_title(self, title: str) -> None:
        """Remove a task by its title."""
        self.tasks = [task for task in self.tasks if task.title != title]

    def count_completed(self) -> int:
        """Count the number of completed tasks."""
        return sum(1 for task in self.tasks if task.status == TaskStatus.COMPLETED)

    def auto_complete_low_priority(self) -> None:
        """Automatically mark all low-priority tasks as completed."""
        for task in self.tasks:
            if task.priority == TaskPriority.LOW:
                task.update_status(TaskStatus.COMPLETED)

    def find_by_priority(self, priority: TaskPriority) -> List[Task]:
        """Find all tasks with a given priority."""
        return [task for task in self.tasks if task.priority == priority]

    def export_task_titles(self, filename: str = "tasks.txt") -> None:
        """Export all task titles to a file."""
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(task.title + "\n")

    def add_random_tag_to_all(self) -> None:
        """Add a random tag to all tasks."""
        tags = ["urgent", "review", "optional", "bug"]
        for task in self.tasks:
            task.tags.append(random.choice(tags))

def main():
    mgr = TaskManager()
    mgr.create_task("Fix login", "Users can’t log in after update", 3, TaskPriority.MEDIUM)
    mgr.create_task("Update docs", "Add API usage examples", 5, TaskPriority.LOW)
    mgr.create_task("Deploy new build", "Push version 2.1", 2, TaskPriority.HIGH)

    mgr.show_tasks()
    mgr.tasks[0].start()
    time.sleep(0.1)
    mgr.tasks[0].stop()
    mgr.tasks[0].print_logs()

    mgr.auto_complete_low_priority()
    mgr.export_task_titles()
    mgr.add_random_tag_to_all()

if __name__ == "__main__":
    main()