from datetime import date
from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Morning walk", 30, 1, "08:00", "daily", date.today())
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Feed Buddy", 10, 2, "09:00", "daily", date.today())
    pet.add_task(task)
    assert len(pet.tasks) == 1