import json
import csv
from abc import ABC, abstractmethod


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class Storage(ABC):
    @abstractmethod
    def save_tasks(self, tasks):
        pass

    @abstractmethod
    def load_tasks(self):
        pass


class JSONStorage(Storage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return [Task(**data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


class CSVStorage(Storage):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["task_id", "title", "description", "due_date", "status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                return [Task(**row) for row in reader]
        except (FileNotFoundError, csv.Error):
            return []


class ToDoApp:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)
        print("Tasks saved successfully!")


if __name__ == "__main__":
    storage = JSONStorage()  # Switch to CSVStorage() if needed
    app = ToDoApp(storage)

    while True:
        print("\nTo-Do Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            app.add_task(Task(task_id, title, description, due_date, status))
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep unchanged): ") or None
            description = input("Enter new Description (leave blank to keep unchanged): ") or None
            due_date = input("Enter new Due Date (leave blank to keep unchanged): ") or None
            status = input("Enter new Status (leave blank to keep unchanged): ") or None
            app.update_task(task_id, title=title, description=description, due_date=due_date, status=status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            app.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            filtered_tasks = app.filter_tasks(status)
            for task in filtered_tasks:
                print(task)
        elif choice == "6":
            app.save_tasks()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
