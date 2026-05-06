"""Unit tests for the todo list application."""

from pathlib import Path
import tempfile
import unittest

from todo_app import TodoList


class TodoListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_dir.name) / "todos.json"
        self.todo_list = TodoList(self.storage_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_task_trims_title_and_stores_item(self) -> None:
        item = self.todo_list.add_task("  Learn Jenkins  ")

        self.assertEqual(item.title, "Learn Jenkins")
        self.assertEqual(item.status, "pending")
        self.assertEqual(len(self.todo_list.list_tasks()), 1)

    def test_add_task_rejects_empty_titles(self) -> None:
        with self.assertRaises(ValueError):
            self.todo_list.add_task("   ")

    def test_complete_task_marks_item_as_completed(self) -> None:
        self.todo_list.add_task("Write tests")

        status = self.todo_list.complete_task(0)

        self.assertEqual(status.status, "completed")
        self.assertEqual(len(self.todo_list.completed_tasks()), 1)
        self.assertEqual(len(self.todo_list.pending_tasks()), 0)

    def test_remove_task_returns_removed_item(self) -> None:
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")

        removed = self.todo_list.remove_task(0)

        self.assertEqual(removed.title, "Task 1")
        self.assertEqual(len(self.todo_list.list_tasks()), 1)
        self.assertEqual(self.todo_list.list_tasks()[0].title, "Task 2")

    def test_task_index_out_of_range_raises_error(self) -> None:
        with self.assertRaises(IndexError):
            self.todo_list.complete_task(0)

    def test_tasks_are_saved_and_reloaded_from_json(self) -> None:
        self.todo_list.add_task("Persist me")
        self.todo_list.complete_task(0)

        reloaded = TodoList(self.storage_path)

        self.assertEqual(len(reloaded.list_tasks()), 1)
        self.assertEqual(reloaded.list_tasks()[0].title, "Persist me")
        self.assertEqual(reloaded.list_tasks()[0].status, "completed")


if __name__ == "__main__":
    unittest.main()