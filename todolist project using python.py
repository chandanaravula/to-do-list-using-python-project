

class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added successfully!")
        else:
            print(f"Task '{task_name}' already exists!")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' removed successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def mark_task_completed(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed!")
        else:
            print(f"Task '{task_name}' not found!")

    def display_tasks(self):
        print("\nTo-Do List:")
        for task, completed in self.tasks.items():
            status = "Completed" if completed else "Pending"
            print(f"- {task}: {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            todo_list.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            todo_list.mark_task_completed(task_name)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()


