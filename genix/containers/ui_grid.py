import genix
import pygame as pg


class UIGrid(genix.UIContainer):
    def __init__(self):
        super().__init__()
        self.set_colour(genix.colours.WHITE)
        self.set_alpha(0)
        self.rows = 0
        self.columns = 0
        self.ui_components = self.components
        self.x_spacing, self.y_spacing = 0, 0
        self.layout_constraint = []

    def add_constraint(self, constraint):
        self.layout_constraint.append(constraint)

    def set_spacing(self, x_spacing=0, y_spacing=0):
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing

    def set_columns(self, column_count):
        self.columns = column_count

    def update_layout(self):

        self.ui_components = self.components
        self.rows = len(self.ui_components) // self.columns
        self.rect.width, self.rect.height = 0, 0
        index = 0
        parent = self
        component = self
        for column in range(self.columns):

            component = self.ui_components[column]
            self.rect.height += component.rect.height

            for row in range(self.rows):
                component = self.ui_components[index]
                parent = component.parent_screen.parent_screen

                component.add_x(row * parent.rect.width * self.x_spacing)
                component.add_y(column * parent.rect.width * self.y_spacing)
                index += 1

        for row in range(self.rows):
            component = self.ui_components[row]
            self.rect.width += component.rect.width

        self.rect.width += ((self.rows-1) * ((parent.rect.width * self.x_spacing)-component.rect.width))
        self.rect.height += ((self.columns-1) * ((parent.rect.width * self.y_spacing)-component.rect.height))

        self.image = pg.transform.smoothscale(self.original_image, self.rect.size)

        for constraint in self.layout_constraint:
            constraint.update_constraint(self)
