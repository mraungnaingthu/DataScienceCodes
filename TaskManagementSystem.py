import time
import functools

# Logging Decorator
def log_calls(func):
    """Logs Function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

# Performance Timing Decorator
def time_execution(func):
    """Measures execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time: .5f} seconds")
        return result
    return wrapper

# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = {}

    # Adding Tasks
    @log_calls
    @time_execution
    def add_tasks(self, task_name, deadline):
        """Add a new task with deadline"""
        self.tasks[task_name] = deadline
        self.view_tasks.cache_clear()
        print(f"Task {task_name} added with deadline: {deadline}")

    # Removing Tasks
    @log_calls
    @time_execution
    def remove_task(self, task_name):
        """ Removes a completed task """
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.view_tasks.cache_clear()
            print(f"Task '{task_name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    #Showing All Tasks
    @functools.lru_cache(maxsize=5)
    @log_calls
    @time_execution
    def view_tasks(self):
        """ Displays all tasks (cached) """
        print("Current Tasks:")
        for task, deadline in self.tasks.items():
            print(f"- {task} (Deadline: {deadline})")

# Main Function to test
if __name__ == "__main__":
    # Testing the Task Manager
    task_manager = TaskManager()
    task_manager.add_tasks("Study Python", "2025-06-10")
    task_manager.add_tasks("Complete JLPT Practice", "2025-06-15")
    task_manager.view_tasks()
    task_manager.remove_task("Study Python")
    task_manager.view_tasks()