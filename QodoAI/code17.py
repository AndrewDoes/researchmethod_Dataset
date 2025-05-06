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
        self.logs.append("Task started")

    def stop(self):
        self.end_time = time.time()
        self.logs.append("Task stopped")

    def log_activity(self, msg):
        self.logs.append(msg)

    def calculate_duration(self):
        return self.end_time - self.start_time

    def update_status(self, s):
        self.status = s
        if s == "completed":
            self.logs.append("Completed")
        elif s == "cancelled":
            self.logs.append("Cancelled")

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
        if self.priority == 1:
            return "Low"
        elif self.priority == 2:
            return "Medium"
        elif self.priority == 3:
            return "High"
        else:
            return "Unknown"

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.last_task = None

    def create_task(self, t, d, due, p=1):
        task = Task(t, d, due, priority=p)
        self.task_list.append(task)
        self.last_task = task

    def show_tasks(self):
        for t in self.task_list:
            t.display_info()
            print("---")

    def remove_task(self, task):
        if task in self.task_list:
            self.task_list.remove(task)

    def remove_task_by_title(self, title):
        for t in self.task_list:
            if t.title == title:
                self.task_list.remove(t)
                return

    def count_completed(self):
        count = 0
        for t in self.task_list:
            if t.status == "completed":
                count += 1
        return count

    def auto_complete_low_priority(self):
        for t in self.task_list:
            if t.priority == 1:
                t.update_status("completed")

    def find_by_priority(self, p):
        found = []
        for t in self.task_list:
            if t.priority == p:
                found.append(t)
        return found

    def export_task_titles(self):
        f = open("tasks.txt", "w")
        for t in self.task_list:
            f.write(t.title + "\n")
        f.close()

    def add_random_tag_to_all(self):
        tags = ["urgent", "review", "optional", "bug"]
        for t in self.task_list:
            t.tags.append(random.choice(tags))

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
