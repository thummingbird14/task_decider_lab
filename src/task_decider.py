from . import tasks

wash_dishes = "Wash Dishes"
cook_dinner = "Cook Dinner"
clean_windows = "Clean Windows"

def get_preferred_option(task_1, task_2):
    task_list = [task_1, task_2]
    if task_1.description == wash_dishes  and task_2.description == cook_dinner in task_list:
        return wash_dishes
    # elif cook_dinner and clean_windows in task_list:
        # return cook_dinner
    # else:
        # return clean_windows
