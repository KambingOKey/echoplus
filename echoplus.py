import subprocess
import time
import os
from datetime import datetime
from threading import Thread

class EchoPlus:
    def __init__(self):
        self.scheduled_tasks = []

    def add_task(self, task_name, command, run_time):
        """Add a task to the schedule."""
        self.scheduled_tasks.append({
            'task_name': task_name,
            'command': command,
            'run_time': run_time
        })
        print(f"Task '{task_name}' scheduled to run at {run_time}")

    def run_task(self, task):
        """Run a specified task."""
        current_time_str = datetime.now().strftime("%H:%M")
        if current_time_str == task['run_time']:
            print(f"Running task: {task['task_name']}")
            try:
                subprocess.run(task['command'], shell=True)
                print(f"Task '{task['task_name']}' completed successfully.")
            except Exception as e:
                print(f"Error running task '{task['task_name']}': {str(e)}")

    def monitor_tasks(self):
        """Continuously monitor and run tasks at their scheduled times."""
        while True:
            for task in self.scheduled_tasks:
                self.run_task(task)
            time.sleep(60)  # Check every minute

    def start(self):
        """Start the EchoPlus scheduler."""
        print("EchoPlus scheduler started.")
        monitor_thread = Thread(target=self.monitor_tasks)
        monitor_thread.daemon = True
        monitor_thread.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Scheduler stopped.")

if __name__ == "__main__":
    echo_plus = EchoPlus()
    echo_plus.add_task("Open Notepad", "notepad.exe", "14:30")
    echo_plus.add_task("Run Custom Script", "python your_script.py", "15:00")
    echo_plus.start()