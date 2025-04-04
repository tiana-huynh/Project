# A class to represent a task
class Task:
    def __init__(self, name, status="Incomplete"):
        self.name = name  # The name of the task
        self.status = status  # Status can be Incomplete or Complete

    def mark_complete(self):
        self.status = "Complete"  # Change the status to Complete

    def __str__(self):
        return f"{self.name} - {self.status}"

# A class to manage a list of tasks
class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store all tasks

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print("Task added!\n")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print("Task marked as complete!\n")
        else:
            print("That task number doesn't exist!\n")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed!\n")
        else:
            print("That task number doesn't exist!\n")

    def display_tasks(self):
        if not self.tasks:
            print("You have no tasks yet.\n")
        else:
            print("Here are your tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
            print("")

# Main function to run the menu
def main():
    todo = ToDoList()  # Create a new to-do list

    while True:
        # Print menu options
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")
        print("")

        # Do something based on user choice
        if choice == "1":
            task_name = input("What task do you want to add? ")
            todo.add_task(task_name)
        elif choice == "2":
            todo.display_tasks()
            task_index = int(input("Which task number is complete? ")) - 1
            todo.mark_task_complete(task_index)
        elif choice == "3":
            todo.display_tasks()
            task_index = int(input("Which task number do you want to remove? ")) - 1
            todo.remove_task(task_index)
        elif choice == "4":
            todo.display_tasks()
        elif choice == "5":
            print("See you later!")
            break
        else:
            print("That's not a valid option. Try again.\n")

if __name__ == "__main__":
    main()
