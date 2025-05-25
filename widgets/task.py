from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from .strike_label import StrikeLabel
from kivy.lang import Builder
from enum import Enum

class TaskStatus(Enum):
    COMPLETED=0
    UNCOMPLETED=1

Builder.load_file('kv/task.kv')

class Task(GridLayout):

    description = StringProperty()

    def __init__(self, description, **kwargs):
        super().__init__(**kwargs)
        self.status = TaskStatus.UNCOMPLETED
        self.description = description


    def change_status(self):
        if self.status == TaskStatus.UNCOMPLETED:
            self.status = TaskStatus.COMPLETED
        
        elif self.status == TaskStatus.COMPLETED:
            self.status = TaskStatus.UNCOMPLETED

