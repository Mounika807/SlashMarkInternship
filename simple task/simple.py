import datetime

class Task:
    def __init__(self, description, priority, status="To Do"):
        self.description = description
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i+1}: {task.description} | Priority: {task.priority} | Status: {task.status}")

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def task_recommendation(self, keyword):
        recommended_tasks = [task for task in self.tasks if keyword in task.description]
        if recommended_tasks:
            print("Recommended Tasks:")
            for i, task in enumerate(recommended_tasks):
                print(f"Task {i+1}: {task.description}")
        else:
            print("No tasks match the provided keyword.")

    def update_task_status(self, task_index, new_status):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = new_status

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Task Recommendation")
        print("6. Update Task Status")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-5, where 5 is highest): "))
            task_manager.add_task(description, priority)
            print("Task added successfully.")

        elif choice == '2':
            task_index = int(input("Enter index of task to remove: ")) - 1
            task_manager.remove_task(task_index)
            print("Task removed successfully.")

        elif choice == '3':
            task_manager.list_tasks()

        elif choice == '4':
            task_manager.prioritize_tasks()
            print("Tasks prioritized successfully.")

        elif choice == '5':
            keyword = input("Enter keyword to search for in task descriptions: ")
            task_manager.task_recommendation(keyword)

        elif choice == '6':
            task_index = int(input("Enter index of task to update: ")) - 1
            new_status = input("Enter new status for the task: ")
            task_manager.update_task_status(task_index, new_status)
            print("Task status updated successfully.")

        elif choice == '7':
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
