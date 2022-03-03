import unittest
from src.tasks import Tasks

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.task_washing_dishes = Tasks("Washing Dishes", 25)

    def test_task_has_description(self):
        self.assertEqual("Washinl Dishes", self.task_washing_dishes.description)

    def test_task_has_duration(self):
        self.assertEqual(20, self.task_washing_dishes.duration)

