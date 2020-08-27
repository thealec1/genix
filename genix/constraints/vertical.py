from genix.constraints.constraint import Constraint


class Vertical(Constraint):
    def __init__(self, y_offset):
        super().__init__()
        self.priority = 2
        self.y_offset = y_offset

    def update_constraint(self, ui_element=None):
        ui_element.add_y(ui_element.parent_screen.rect.height * self.y_offset)
