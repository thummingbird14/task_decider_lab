import unittest
from src import task_decider

class TestTaskDecider(unittest.TestCase):

    def setUp(self):
        self.washing_dishes = task_decider.TaskDecider("Wash Dishes", "Cook Dinner")

    def test_Wash_Dishes_Cook_Dinner_compare(self):
        self.assertEqual("Wash Dishes", self.washing_dishes.get_preferred_option())

