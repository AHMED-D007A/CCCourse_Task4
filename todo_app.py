"""Simple todo list application."""

from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class TodoItem:
    """Represents a single todo item."""

    title: str
    status: str = field(default="pending")

    def to_dict(self) -> dict[str, object]:
        return {"title": self.title, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TodoItem:
        return cls(title=str(data["title"]), status=str(data.get("status", "pending")))


class TodoList:
    """Todo list manager backed by a JSON file."""

    def __init__(self, storage_path: str | Path = "todos.json") -> None:
        self._storage_path = Path(storage_path)
        self._items: list[TodoItem] = []
        self._load()

    def add_task(self, title: str) -> TodoItem:
        """Add a new task and return it."""
        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Task title cannot be empty")

        item = TodoItem(title=cleaned_title)
        self._items.append(item)
        self._save()
        return item

    def complete_task(self, index: int) -> TodoItem:
        """Mark a task as completed by index."""
        item = self._get_item(index)
        item.status = "completed"
        self._save()
        return item

    def remove_task(self, index: int) -> TodoItem:
        """Remove a task by index and return it."""
        self._validate_index(index)
        removed_item = self._items.pop(index)
        self._save()
        return removed_item

    def list_tasks(self) -> list[TodoItem]:
        """Return all tasks in insertion order."""
        return list(self._items)

    def pending_tasks(self) -> list[TodoItem]:
        """Return only incomplete tasks."""
        return [item for item in self._items if item.status == "pending"]

    def completed_tasks(self) -> list[TodoItem]:
        """Return only completed tasks."""
        return [item for item in self._items if item.status == "completed"]

    def _get_item(self, index: int) -> TodoItem:
        self._validate_index(index)
        return self._items[index]

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise IndexError("Task index out of range")

    def _load(self) -> None:
        if not self._storage_path.exists():
            return

        raw_content = self._storage_path.read_text(encoding="utf-8").strip()
        if not raw_content:
            return

        data = json.loads(raw_content)
        self._items = [TodoItem.from_dict(item) for item in data]

    def _save(self) -> None:
        self._storage_path.write_text(
            json.dumps([item.to_dict() for item in self._items], indent=2),
            encoding="utf-8",
        )


def _format_tasks(items: list[TodoItem]) -> str:
    lines = []
    for position, item in enumerate(items, start=1):
        status = "done" if item.status == "completed" else "pending"
        lines.append(f"{position}. [{status}] {item.title}")
    return "\n".join(lines) if lines else "No tasks yet."


def main() -> None:
    """Small demo CLI for the todo list."""
    todo_list = TodoList()

    print("Todo List")
    print("Commands: add, complete, remove, list, quit")

    while True:
        command = input("> ").strip().lower()

        if command == "add":
            title = input("Task title: ")
            try:
                todo_list.add_task(title)
                print("Task added.")
            except ValueError as exc:
                print(exc)
        elif command == "complete":
            try:
                index = int(input("Task number to complete: ")) - 1
                todo_list.complete_task(index)
                print("Task completed.")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif command == "remove":
            try:
                index = int(input("Task number to remove: ")) - 1
                removed = todo_list.remove_task(index)
                print(f"Removed: {removed.title}")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif command == "list":
            print(_format_tasks(todo_list.list_tasks()))
        elif command == "quit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()