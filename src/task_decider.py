class TaskDecider():
    
    def __init__(self, task_1, task_2):
        self.task_1 = task_1
        self.task_2 = task_2
        self.wash_dishes = "Wash dishes"
        self.cook_dinner = "Cook Dinner"
        self.clean_windows = "Clean Windows"

    def get_preferred_option(self):
        task_list = [self.task_1, self.task_2]
        if self.wash_dishes and self.cook_dinner in task_list:
            return self.wash_dishes
        elif self.cook_dinner and self.clean_windows in task_list:
            return self.cook_dinner
        else:
            return self.clean_windows
                
        
