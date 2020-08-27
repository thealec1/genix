from genix.constraints.constraint import Constraint
import pygame as pg


class HeightRatio(Constraint):
    def __init__(self):
        super().__init__()
        self.priority = 1

    def update_constraint(self, ui_element=None):
        ui_element.rect.height = ui_element.rect.width
        ui_element.image = pg.transform.smoothscale(ui_element.original_image, ui_element.rect.size)
