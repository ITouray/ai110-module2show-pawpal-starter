"""PawPal+ — pet care planning assistant.

Class skeleton based on diagrams/uml.mmd.
Four core classes: Owner, Pet, CareTask, Scheduler.
Method bodies are intentionally empty stubs to be implemented next.
"""


class CareTask:
    """A single thing that needs to happen for a pet."""

    def __init__(self, title, duration_minutes, priority="medium", preferred_time=None):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority            # "low" | "medium" | "high"
        self.preferred_time = preferred_time
        self.completed = False

    def mark_complete(self):
        """Mark this task as done."""
        pass

    def priority_weight(self):
        """Return a numeric weight so tasks can be ordered by priority."""
        pass


class Pet:
    """A pet that has care tasks."""

    def __init__(self, name, species, age=None):
        self.name = name
        self.species = species
        self.age = age
        self.tasks = []                     # list[CareTask]

    def add_task(self, task):
        """Attach a CareTask to this pet."""
        pass

    def list_tasks(self):
        """Return all tasks for this pet."""
        pass


class Owner:
    """The pet owner, with pets and scheduling preferences/constraints."""

    def __init__(self, name, available_minutes=0):
        self.name = name
        self.pets = []                      # list[Pet]
        self.preferences = {}
        self.available_minutes = available_minutes

    def add_pet(self, pet):
        """Add a pet to this owner."""
        pass

    def set_preference(self, key, value):
        """Store an owner preference (e.g. preferred walk time)."""
        pass

    def get_available_minutes(self):
        """Return how many minutes the owner has for care today."""
        pass


class Scheduler:
    """Builds and explains a daily care plan from the owner's tasks/constraints."""

    def __init__(self, owner):
        self.owner = owner
        self.tasks = []                     # list[CareTask] collected from pets

    def build_plan(self):
        """Choose and order tasks that fit the owner's time budget."""
        pass

    def order_by_priority(self):
        """Return tasks sorted high -> low priority."""
        pass

    def fits_in_budget(self, task):
        """Return True if the task fits in the remaining time budget."""
        pass

    def explain_plan(self):
        """Return a human-readable explanation of why/when each task was chosen."""
        pass
