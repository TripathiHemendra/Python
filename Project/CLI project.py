# Task class to represent each task
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False  # Task starts as incomplete

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"Task: {self.title} | Status: {status}"


# ToDoList class to manage the task list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f'Added task: "{title}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f'Marked task "{self.tasks[index].title}" as complete.')
        else:
            print("Invalid task index.")


# Main CLI loop
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter the task title: ")
            todo_list.add_task(title)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to mark complete: ")) - 1
                todo_list.complete_task(task_num)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Entry point of the program
# if __name__ == "__main__":
main()


# Here's a simple Python project idea: Building a To-Do List CLI Application using object-oriented programming.

# Project Overview
# This project is a Command Line Interface (CLI) based To-Do List application. Users can add tasks, view tasks, and mark tasks as complete. We'll use Python's input() function for CLI interaction and store tasks in a list.

# Code Structure
# Task class: Represents a task with attributes like title and status (complete or incomplete).
# ToDoList class: Manages the list of tasks with methods to add, view, and complete tasks.
# Main CLI loop: Accepts user commands to interact with the task list.

# Explanation
# Task Class:

# Each task has a title and a completed status (initially set to False).
# mark_complete(): Marks the task as complete by setting self.completed to True.
# __str__(): Returns a formatted string representation of the task for display.
# ToDoList Class:

# self.tasks: A list that holds all task objects.
# add_task(title): Adds a new task to the task list.
# view_tasks(): Displays all tasks, showing their title and completion status.
# complete_task(index): Marks a task at the given index as complete.
# Main CLI Loop:

# Displays a menu and takes input from the user.
# Based on the user’s choice, it adds, views, or marks tasks as complete.
# Loop continues until the user chooses to exit.
# Running the Program
# When you run the program, the CLI provides the following menu:

# Add a task: The user can input a new task title.
# View tasks: Lists all the tasks with their status.
# Mark task complete: Marks a task as complete by entering its number.
# Exit: Exits the program.
# This project can be easily extended with more features like task priority, due dates, or saving tasks to a file for persistence.







