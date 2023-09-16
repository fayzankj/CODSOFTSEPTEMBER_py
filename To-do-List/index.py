def add_task(task, todo_list):
    with open(todo_list, 'a') as file:
        file.write(task + '\n')

def list_tasks(todo_list):
    try:
        with open(todo_list, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


def mark_done(task_number, todo_list):
    try:
        with open(todo_list, 'r') as file:
            tasks = file.readlines()
        if task_number > 0 and task_number <= len(tasks):
            tasks[task_number - 1] = "[Done] " + tasks[task_number - 1][6:]
            with open(todo_list, 'w') as file:
                file.writelines(tasks)
            print(f"Task {task_number} marked as done.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


def delete_task(task_number, todo_list):
    try:
        with open(todo_list, 'r') as file:
            tasks = file.readlines()
        if task_number > 0 and task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            with open(todo_list, 'w') as file:
                file.writelines(tasks)
            print(f"Task {task_number} deleted: {deleted_task.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


def main():
    todo_list = "todo.txt"
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task, todo_list)
        elif choice == "2":
            list_tasks(todo_list)
        elif choice == "3":
            list_tasks(todo_list)
            task_number = int(input("Enter the task number to mark as done: "))
            mark_done(task_number, todo_list)
        elif choice == "4":
            list_tasks(todo_list)
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number, todo_list)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
