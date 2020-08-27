from genix.constraints.constraint import Constraint
from genix.containers.ui_grid import UIGrid
import pygame as pg


class RelativeWidth(Constraint):

    def __init__(self, width_percent):
        super().__init__()
        self.width_percent = width_percent

    def update_constraint(self, ui_element=None):

        parent = ui_element.parent_screen

        if isinstance(parent, UIGrid):
            parent = ui_element.parent_screen.parent_screen

        ui_element.rect.width = parent.rect.width * self.width_percent
        ui_element.image = pg.transform.smoothscale(ui_element.original_image, ui_element.rect.size)
