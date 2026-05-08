# Todo Application - CCCourse Task 4

A simple, file-based todo list application built with Python, featuring comprehensive unit tests and CI/CD integration with Jenkins.

## Overview

This project is part of CCCourse Task 4, which focuses on implementing CI/CD pipelines using Jenkins. The application demonstrates:
- Clean Python code with type hints
- Unit testing best practices
- Git version control
- Automated CI/CD pipeline execution

## Features

- ✅ Add tasks to your todo list
- ✅ Mark tasks as completed
- ✅ Remove tasks
- ✅ View all tasks or filter by status (pending/completed)
- ✅ Persistent storage in JSON format
- ✅ Input validation with meaningful error messages
- ✅ Comprehensive unit test coverage

## Project Structure

```
CCCourse_Task4/
├── todo_app.py              # Main application with TodoList and TodoItem classes
├── test_todo_app.py         # Unit tests for the todo application
├── todos.json               # Persistent storage file (JSON)
├── Jenkinsfile              # CI/CD pipeline configuration
├── README.md                # This file
└── repository_link.txt      # Link to the remote repository
```

## Requirements

- Python 3.8 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AHMED-D007A/CCCourse_Task4.git
   cd CCCourse_Task4
   ```

2. No additional setup required - the application uses only Python standard library modules.

## Usage

### Python API

```python
from todo_app import TodoList

# Create a todo list instance
todo_list = TodoList("todos.json")

# Add tasks
task1 = todo_list.add_task("Learn Jenkins")
task2 = todo_list.add_task("Write unit tests")

# List all tasks
all_tasks = todo_list.list_tasks()

# View pending tasks
pending = todo_list.pending_tasks()

# Mark a task as completed
todo_list.complete_task(0)

# View completed tasks
completed = todo_list.completed_tasks()

# Remove a task
todo_list.remove_task(0)
```

### API Reference

#### `TodoItem`
Represents a single todo item with a title and status.

**Attributes:**
- `title` (str): The task description
- `status` (str): Task status - "pending" or "completed"

#### `TodoList`
Manages a collection of todo items with persistent JSON storage.

**Methods:**
- `add_task(title: str) -> TodoItem`: Add a new task
- `complete_task(index: int) -> TodoItem`: Mark task as completed
- `remove_task(index: int) -> TodoItem`: Remove and return a task
- `list_tasks() -> list[TodoItem]`: Get all tasks
- `pending_tasks() -> list[TodoItem]`: Get incomplete tasks
- `completed_tasks() -> list[TodoItem]`: Get completed tasks

## Running Tests

Execute the unit tests using Python's unittest framework:

```bash
python3 -m unittest -v
```

### Test Coverage

The test suite includes:
- Adding tasks with whitespace trimming
- Rejecting empty task titles
- Marking tasks as completed
- Removing tasks
- Index validation
- JSON persistence and reloading

## CI/CD Pipeline

This project includes a Jenkins pipeline (`Jenkinsfile`) that automates testing and integration.

### Pipeline Stages

1. **Clone/Pull Repository**: Fetches the latest code from the main branch
2. **Run Unit Tests**: Executes all unit tests and reports results

### Running the Pipeline

The pipeline is triggered automatically when changes are pushed to the repository. To run manually in Jenkins:

1. Navigate to the job in Jenkins
2. Click "Build Now"
3. Monitor the build progress in the console output
4. Review test results

## Data Storage

Tasks are persisted in `todos.json` in the following format:

```json
[
  {
    "title": "Learn Jenkins",
    "status": "pending"
  },
  {
    "title": "Write unit tests",
    "status": "completed"
  }
]
```

## Code Quality

The project follows Python best practices:
- Type hints for all functions and methods
- Dataclass usage for clean data structures
- Comprehensive error handling
- Clear docstrings for all classes and methods
- Clean separation of concerns
