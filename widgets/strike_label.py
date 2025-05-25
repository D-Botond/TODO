from kivy.uix.label import Label
from kivy.graphics import Color, Line

class StrikeLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(pos=self.update_line, 
                  size=self.update_line, 
                  text=self.update_line)

        with self.canvas.after:
            self.strike_color = Color(1, 1, 1, 1) 
            self.strike_line = Line(points=[])

    def update_line(self, *args):
        x1 = self.x
        x2 = self.right
        y = self.center_y
        self.strike_line.points = [x1, y, x2, y]