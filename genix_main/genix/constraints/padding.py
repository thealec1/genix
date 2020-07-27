from genix.constraints.constraint import Constraint
import pygame as pg


class Padding(Constraint):
    def __init__(self, spacing, ui_components, row_count):
        self.spacing = spacing
        self.ui_components = ui_components
        self.rows = row_count
        self.columns = len(self.ui_components) // row_count

    def update_constraint(self, ui_element=None):

        # component = None
        # parent = None
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                component = self.ui_components[index]
                parent = component.parent_screen
                component.add_x(column * (parent.rect.width * self.spacing))
                component.add_y(row * (parent.rect.width * self.spacing))
                index += 1

        # spacer = parent.rect.width * self.spacing
        # print(self.columns)
        # ui_element.rect.width = (component.rect.width * self.columns) + (spacer * (self.columns-1))
        # ui_element.rect.height = (component.rect.height * self.rows) + (spacer * (self.rows-1))
        # ui_element.image = pg.transform.smoothscale(ui_element.original_image, ui_element.rect.size)
