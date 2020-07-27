from genix.constraints.constraint import Constraint


class Vertical(Constraint):

    def __init__(self, y_offset):
        self.y_offset = y_offset

    def update_constraint(self, ui_element=None):
        # ui_element.rect.y += ui_element.parent_screen.rect.height * self.y_offset
        ui_element.add_y(ui_element.parent_screen.rect.height * self.y_offset)
