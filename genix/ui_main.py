import pygame as pg


class UIMain:
    """
    The main component behind all of the user interface components

    Contains both the visible and non visible component lists for all created components.
    """

    win = None
    ui_elements = pg.sprite.Group()
    visible_ui_elements = pg.sprite.LayeredUpdates()
    is_client_clicking = False

    def __init__(self, main_window):
        UIMain.win = main_window

    @staticmethod
    def main():

        UIMain.ui_elements.update()
        UIMain.visible_ui_elements.draw(UIMain.win.screen)

    @staticmethod
    def do_events(event):
        """
        Gets a pygame event and does something with it

        :param event: A pygame event
        :return:
        """

        if event.type == pg.VIDEORESIZE:
            UIMain.win.rect.width, UIMain.win.rect.height = event.dict["size"]
            UIMain.ui_elements.update("constrain")
            UIMain.ui_elements.update("layout")

        if event.type == pg.KEYDOWN and event.key == UIMain.win.fullscreen_bind:
            UIMain.win.toggle_fullscreen()

        for ui_element in UIMain.visible_ui_elements:

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    UIMain.is_client_clicking = True
                    if ui_element.hover:
                        ui_element.on_click()

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    UIMain.is_client_clicking = False
                    if ui_element.hover:
                        ui_element.on_release()
