import json
import csv

# File paths
json_file = "tasks.json"
csv_file = "tasks.csv"

# Load tasks from JSON file
def load_tasks():
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(json_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    print("\nTask List:")
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<8}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<8}")
    print()

# Modify a task (mark complete/incomplete)
def modify_task(tasks, task_id, completed_status):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = completed_status
            save_tasks(tasks)
            print(f"Task '{task['task']}' updated successfully!")
            return
    print("Task ID not found.")

# Calculate task statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {round(avg_priority, 2)}\n")

# Convert JSON data to CSV
def convert_to_csv(tasks):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])  # Header
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks have been saved to {csv_file} ")

# Main Execution
tasks = load_tasks()
display_tasks(tasks)
calculate_stats(tasks)

# Example modifications
modify_task(tasks, 1, True)  # Mark task ID 1 as completed
convert_to_csv(tasks)
