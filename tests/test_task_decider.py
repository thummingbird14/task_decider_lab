import unittest
from src import task_decider
from src import tasks


class TestTaskDecider(unittest.TestCase):

    def setUp(self):
        self.task_object_1 = tasks.Tasks("Wash Dishes", 25)
        self.task_object_2 = tasks.Tasks("Cook Dinner", 40)


    def test_wash_Dishes_Cook_Dinner_compare(self):
        self.assertEqual("Wash Dishes", self.get_preferred_option(self.task_object_1),
        self.task_object_2)

    # def test_clean_Windows_Cook_Dinner_compare(self):
        # self.assertEqual("Clean Windows", self.cook_dinner.get_preferred_option())
    


