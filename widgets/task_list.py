from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from .task import Task

Builder.load_file('kv/task_list.kv')

class TaskList(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        for i in range(10):
            self.add_widget(Task('Task '+str(i)))
            

