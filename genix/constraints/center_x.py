from genix.constraints.constraint import Constraint


class CenterX(Constraint):
    def __init__(self):
        super().__init__()
        self.priority = 2

    def update_constraint(self, ui_element=None):
        ui_element.add_x((ui_element.parent_screen.rect.width//2)-(ui_element.image.get_width()//2))
