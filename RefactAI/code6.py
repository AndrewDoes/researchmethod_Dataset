tasks = []
task_status = []
priority = []

def start_app():
    print("Welcome to the Messy To-Do List!")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Remove Task\n5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

def add_task():
    task = input("Enter task description: ")
    prio = input("Enter priority (High, Medium, Low): ")
    if prio not in ["High", "Medium", "Low"]:
        print("Invalid priority, defaulting to Low.")
        prio = "Low"
    tasks.append(task)
    task_status.append(False)
    priority.append(prio)
    print(f"Task '{task}' added with priority {prio}.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    print("\n--- To-Do List ---")
    for i in range(len(tasks)):
        status = "Done" if task_status[i] else "Not Done"
        print(f"{i+1}. {tasks[i]} - {status} - Priority: {priority[i]}")

def mark_done():
    if len(tasks) == 0:
        print("No tasks to mark.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            task_status[task_num] = True
            print(f"Task '{tasks[task_num]}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            task_status.pop(task_num)
            priority.pop(task_num)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

start_app()
