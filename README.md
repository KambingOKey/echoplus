# EchoPlus

EchoPlus is a Python program designed to automate the execution of scripts or programs at specific times on Windows. It continuously monitors scheduled tasks and runs them at the designated times.

## Features

- Schedule tasks to run at specific times
- Execute any command-line script or program
- Simple, lightweight, and easy to use

## Requirements

- Python 3.x
- Windows OS

## Installation

1. Clone this repository or download the `echoplus.py` file.
2. Ensure that Python is installed on your system and is added to your system's PATH.

## Usage

1. Open `echoplus.py` in a text editor.
2. Add your tasks using the `add_task` method. Each task requires:
   - A `task_name` for identification
   - A `command` to execute (e.g., `'notepad.exe'` or `'python your_script.py'`)
   - A `run_time` in the format `HH:MM` (24-hour format)
3. Save your changes and run `echoplus.py` using Python.

```bash
python echoplus.py
```

4. The scheduler will start and monitor the tasks. It will run each task at its scheduled time.

## Example

To schedule a task that opens Notepad at 2:30 PM and runs a custom script at 3:00 PM, modify the `echoplus.py` file as follows:

```python
if __name__ == "__main__":
    echo_plus = EchoPlus()
    echo_plus.add_task("Open Notepad", "notepad.exe", "14:30")
    echo_plus.add_task("Run Custom Script", "python your_script.py", "15:00")
    echo_plus.start()
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.