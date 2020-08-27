from genix.constraints.constraint import Constraint


class Centered(Constraint):
    """
    Instead of having to use both the CenterX() and CenterY() constraints,
    this will center a component to it's parent on both the x and y.
    """
    def __init__(self):
        super().__init__()
        self.priority = 2

    def update_constraint(self, ui_element=None):
        ui_element.add_x((ui_element.parent_screen.rect.width//2) - (ui_element.image.get_width()//2))
        ui_element.add_y((ui_element.parent_screen.rect.height//2) - (ui_element.image.get_height()//2))
