import time
import random

class Task:
    def __init__(self, title, desc, due, status="pending", priority=1):
        self.title = title
        self.desc = desc
        self.due = due
        self.status = status
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

    def log_activity(self, msg):
        self.logs.append(msg)

    def calculate_duration(self):
        return self.end_time - self.start_time

    def update_status(self, status):
        self.status = status
        if status == "completed":
            self.log_activity("Completed")
        elif status == "cancelled":
            self.log_activity("Cancelled")

    def display_info(self):
        print("Title:", self.title)
        print("Description:", self.desc)
        print("Due:", self.due)
        print("Priority:", self.priority)
        print("Status:", self.status)

    def print_logs(self):
        for log in self.logs:
            print(log)

    def delay_due(self, days):
        self.due += days

    def get_priority_value(self):
        priority_values = {1: "Low", 2: "Medium", 3: "High"}
        return priority_values.get(self.priority, "Unknown")

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.last_task = None

    def create_task(self, title, desc, due, priority=1):
        task = Task(title, desc, due, priority=priority)
        self.task_list.append(task)
        self.last_task = task

    def show_tasks(self):
        for task in self.task_list:
            task.display_info()
            print("---")

    def remove_task(self, task):
        if task in self.task_list:
            self.task_list.remove(task)

    def remove_task_by_title(self, title):
        for task in self.task_list:
            if task.title == title:
                self.task_list.remove(task)
                return

    def count_completed(self):
        return sum(1 for task in self.task_list if task.status == "completed")

    def auto_complete_low_priority(self):
        for task in self.task_list:
            if task.priority == 1:
                task.update_status("completed")

    def find_by_priority(self, priority):
        return [task for task in self.task_list if task.priority == priority]

    def export_task_titles(self):
        with open("tasks.txt", "w") as f:
            for task in self.task_list:
                f.write(task.title + "\n")

    def add_random_tag_to_all(self):
        tags = ["urgent", "review", "optional", "bug"]
        for task in self.task_list:
            task.tags.append(random.choice(tags))
            

# Main flow
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