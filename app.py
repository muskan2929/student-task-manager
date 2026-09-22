tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

print("Student Task Manager")
