tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

print("My Student Task Manager")
print("Welcome to Student Task Manager")
def delete_task():
    index = int(input("Enter task number: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted!")
