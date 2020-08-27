import pygame as pg
from genix.components.ui_component import UIComponent
from genix.constraints.relative_width import RelativeWidth
from genix.constraints.relative_height import RelativeHeight


class UIText(UIComponent):

    def __init__(self, text="Genix!"):
        super().__init__()
        self.text = text
        self.colour = (255, 255, 255)
        self.size = 12
        self.font = "arial"
        self.bold = False
        self.italic = False
        self.updated = False
        self.parent_width, self.parent_height = 0, 0
        self.update_text()

    def set_scale(self, scale):
        self.image = pg.transform.smoothscale(self.image, scale)

    def set_text(self, text):
        self.text = text
        self.update_text()

    def set_colour(self, colour_value):
        self.colour = colour_value
        self.update_text()

    def set_bold(self, is_bold):
        self.bold = is_bold
        self.update_text()

    def set_italic(self, is_italic):
        self.italic = is_italic
        self.update_text()

    def set_size(self, size):
        self.size = size
        self.update_text()

    def set_font(self, font):
        self.font = font
        self.update_text()

    def set_parent_sizes(self, width, height):
        if not self.updated:
            self.parent_width, self.parent_height = width, height
            self.updated = True
            self.set_constraint_values()

    def set_constraint_values(self):
        if self.parent_width != 0 and self.parent_height != 0:

            w_percent = self.rect.width / self.parent_width
            h_percent = self.rect.height / self.parent_height

            # If we found the constraint already added to the list, we modify it's percent
            # instead of adding a new instance.

            found_element = False

            for constraint in self.constraints:

                index = self.constraints.index(constraint)

                if isinstance(constraint, RelativeWidth):
                    found_element = True
                    self.constraints[index].width_percent = w_percent

                if isinstance(constraint, RelativeHeight):
                    self.constraints[index].height_precent = h_percent

            if not found_element:
                self.add_constraint(RelativeWidth(w_percent))
                self.add_constraint(RelativeHeight(h_percent))

    def update_text(self):
        font = pg.font.SysFont(self.font, self.size, self.bold, self.italic)
        self.original_image = font.render(str(self.text), 1, self.colour)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.set_constraint_values()
        self.update_constraints()
