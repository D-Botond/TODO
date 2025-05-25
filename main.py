from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


from widgets.main_layout import MainLayout
from widgets.task_list import TaskList


class TodoApp(App):
    def build(self):
        return MainLayout()
    
if __name__ == '__main__':
    TodoApp().run()