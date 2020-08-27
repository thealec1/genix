from genix.constraints.constraint import Constraint
from genix.containers.ui_grid import UIGrid
import pygame as pg


class RelativeHeight(Constraint):

    def __init__(self, height_percent):
        super().__init__()
        self.height_percent = height_percent

    def update_constraint(self, ui_element=None):

        parent = ui_element.parent_screen

        if isinstance(parent, UIGrid):
            parent = ui_element.parent_screen.parent_screen

        ui_element.rect.height = parent.rect.height * self.height_percent
        ui_element.image = pg.transform.smoothscale(ui_element.original_image, ui_element.rect.size)
