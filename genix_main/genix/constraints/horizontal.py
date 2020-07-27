from genix.constraints.constraint import Constraint


class Horizontal(Constraint):

    def __init__(self, x_offset):
        self.x_offset = x_offset

    def update_constraint(self, ui_element=None):
        ui_element.rect.x += ui_element.parent_screen.rect.width * self.x_offset
