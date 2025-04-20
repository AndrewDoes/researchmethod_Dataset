tasks = []
priorities = []

def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
        option = input("Choose an option: ")
        
        if option == "1":
            task_name = input("Enter task name: ")
            task_priority = input("Enter priority (High, Medium, Low): ")
            if task_priority not in ["High", "Medium", "Low"]:
                print("Invalid priority! Defaulting to Medium.")
                task_priority = "Medium"
            tasks.append(task_name)
            priorities.append(task_priority)
            print(f"Task '{task_name}' added with priority {task_priority}.")
        
        elif option == "2":
            if len(tasks) == 0:
                print("No tasks available.")
                continue
            print("\nTasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]} - Priority: {priorities[i]}")
        
        elif option == "3":
            if len(tasks) == 0:
                print("No tasks to complete.")
                continue
            task_number = input("Enter task number to mark as complete: ")
            if not task_number.isdigit() or int(task_number) < 1 or int(task_number) > len(tasks):
                print("Invalid task number!")
                continue
            index = int(task_number) - 1
            print(f"Task '{tasks[index]}' marked as complete.")
            tasks.pop(index)
            priorities.pop(index)
        
        elif option == "4":
            if len(tasks) == 0:
                print("No tasks to remove.")
                continue
            task_number = input("Enter task number to remove: ")
            if not task_number.isdigit() or int(task_number) < 1 or int(task_number) > len(tasks):
                print("Invalid task number!")
                continue
            index = int(task_number) - 1
            print(f"Task '{tasks[index]}' removed.")
            tasks.pop(index)
            priorities.pop(index)
        
        elif option == "5":
            print("Exiting Task Scheduler...")
            break
        else:
            print("Invalid choice! Try again.")

menu()
