from genix.constraints.constraint import Constraint


class CenterY(Constraint):

    def update_constraint(self, ui_element=None):
        # ui_element.rect.y += (ui_element.parent_screen.rect.height//2) - (ui_element.image.get_height()//2)
        ui_element.add_y((ui_element.parent_screen.rect.height//2) - (ui_element.image.get_height()//2))
