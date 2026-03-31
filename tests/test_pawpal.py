from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    task = Task("Morning walk", 30, 1, "08:00", "daily", date.today())
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Feed Buddy", 10, 2, "09:00", "daily", date.today())
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sorting_correctness():
    owner = Owner("Kimberly", 90, "Morning tasks preferred")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    task1 = Task("Feed Buddy", 10, 2, "09:00", "daily", date.today())
    task2 = Task("Morning walk", 30, 1, "08:00", "daily", date.today())
    task3 = Task("Brush Buddy", 15, 3, "07:30", "weekly", date.today())

    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].time == "07:30"
    assert sorted_tasks[1].time == "08:00"
    assert sorted_tasks[2].time == "09:00"


def test_recurrence_logic_daily_task():
    owner = Owner("Kimberly", 90, "Morning tasks preferred")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)

    original_task = Task("Morning walk", 30, 1, "08:00", "daily", date.today())
    pet.add_task(original_task)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete("Buddy", "Morning walk")

    assert len(pet.tasks) == 2
    assert pet.tasks[0].completed is True
    assert pet.tasks[1].description == "Morning walk"
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)
    assert pet.tasks[1].completed is False


def test_conflict_detection():
    owner = Owner("Kimberly", 90, "Morning tasks preferred")
    dog = Pet("Buddy", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    owner.add_pet(dog)
    owner.add_pet(cat)

    task1 = Task("Morning walk", 30, 1, "08:00", "daily", date.today())
    task2 = Task("Brush Luna", 10, 2, "08:00", "weekly", date.today())

    dog.add_task(task1)
    cat.add_task(task2)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]