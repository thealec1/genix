from genix.components.ui_component import UIComponent
import pygame as pg


class UIText(UIComponent):

    def __init__(self, text="Genix!"):
        super().__init__()
        self.text = text
        self.colour = (255, 255, 255)
        self.size = 12
        self.font = "arial"
        self.bold = False
        self.italic = False
        self.update_text()

    def set_scale(self, scale):
        self.image = pg.transform.smoothscale(self.image, scale)

    def set_text(self, text):
        self.text = text

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

    def update_text(self):
        font = pg.font.SysFont(self.font, self.size, self.bold, self.italic)
        self.original_image = font.render(str(self.text), 1, self.colour)
        self.image = self.original_image
        self.rect = self.image.get_rect()
