try:
    import win32con
    import win32gui

except ModuleNotFoundError as e:
    print(e)
    print("Genix Error: Couldn't open win32con and win32gui.  Some features may not work!  Try using pywin32 package.")

import pygame as pg


class UIWindow(pg.sprite.Sprite):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.screen = pg.display.set_mode((width, height))
        self.icon = None
        self.title = "Genix Window!"
        self.set_title(self.title)
        self.rect = pg.Surface((0, 0)).get_rect()
        self.fullscreen = False
        self.fullscreen_bind = pg.K_F11

        if width == 0 and height == 0:
            self.set_window()

    def set_fullscreen_bind(self, binding):
        self.fullscreen_bind = binding

    def set_icon(self, surface):
        self.icon = surface
        pg.display.set_icon(surface)

    def set_title(self, title):
        self.title = title
        pg.display.set_caption(self.title)

    def set_fullscreen(self):
        self.fullscreen = True
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    def set_resizable(self):
        self.fullscreen = False
        self.screen = pg.display.set_mode((0, 0), pg.RESIZABLE)

    @staticmethod
    def set_maximize():
        try:
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MAXIMIZE)

        except NameError as er:
            print(er)
            print("Genix Error: Couldn't maximize screen!")

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.set_resizable()
            self.set_maximize()
        else:
            self.set_fullscreen()

    def set_window(self):

        display_size = pg.display.get_surface()

        self.rect.width = display_size.get_size()[0]
        self.rect.height = display_size.get_size()[1]

        self.screen = pg.display.set_mode((self.rect.width, self.rect.height), pg.RESIZABLE)

        self.set_maximize()
