from genix.ui_main import UIMain
import genix
import pygame as pg


class UIComponent(pg.sprite.Sprite):
    """
    The most basic ui element from which every other element derives from
    """

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        UIMain.visible_ui_elements.add(self)
        UIMain.ui_elements.add(self)

        self.original_image = pg.Surface((10, 10))
        self.image = self.original_image

        self.rect = self.image.get_rect()

        self.parent_screen = UIMain.win
        self.constraints = []

        self.alpha_value = None
        self.surface = None
        self.layout = None
        self.tooltip = None

        self.is_clicking = False
        self.hover = False
        self.can_move = False
        self.last_click_x, self.last_click_y = 0, 0

        # Component events are declared here but should be put into a dict eventually
        self.click_event = None
        self.release_event = None
        self.unhover_event = None
        self.hovering_event = None
        self.hover_event = None
        self.tick_event = None

    def update(self, mode=""):
        """
        Called every tick and handles:
            constraints,
            layouts,
            input events,
            alpha channel,
            ui animations

        :param mode: Whether the ui components should be repositioned.
                    Usually this is true when the display changes size
        :return: None
        """

        if mode == "layout":
            if self.layout is not None:
                self.layout.update_constraint(self)

            if isinstance(self, genix.UIGrid):
                self.update_layout()

        if mode == "constrain":

            self.rect.x, self.rect.y = self.parent_screen.rect.x, self.parent_screen.rect.y

            for constraint in self.constraints:
                constraint.update_constraint(self)

            if self.alpha_value is not None:
                self.set_alpha(self.alpha_value)

        if self.tick_event is not None:
            self.tick_event()

        if not UIMain.is_client_clicking:
            self.is_clicking = False

        if UIMain.is_client_clicking and self.is_clicking:
            if self.can_move:
                self.drag_drop()

        if self.rect.collidepoint(pg.mouse.get_pos()) and self in UIMain.visible_ui_elements:
            self.on_hover()

        else:
            if self.hover:
                self.on_unhover()
            self.hover = False

    def add_x(self, transform_value=0):
        """
        Adds to the x value of this component

        UIComponent method overrides this, which adds to all of it's children

        :param transform_value: The value to change the x by
        :return: None
        """
        self.rect.x += transform_value

    def add_y(self, transform_value=0):
        """
        Adds to the y value of this component

        UIComponent method overrides this, which adds to all of it's children

        :param transform_value: The value to change the y by
        :return: None
        """
        self.rect.y += transform_value

    def add_constraint(self, constraint):
        """
        Adds a constraint to this ui component, it will be updated when the display
        changes size

        :param constraint: An instance of a constraint subclass (ie: CenterX)
        :return: None
        """
        self.constraints.append(constraint)

    def add_layout(self, layout):
        """
        Similar to constraints, but they format components that are parented
        :return:
        """
        self.layout = layout

    def drag_drop(self):
        mouse_x, mouse_y, = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
        self.add_x(self.rect.x * -1)
        self.add_y(self.rect.y * -1)
        self.add_x(mouse_x - self.last_click_x)
        self.add_y(mouse_y - self.last_click_y)

    def set_move(self, can_move):
        self.can_move = can_move

    def set_colour(self, colour_value):
        """
        Changes the colour of this component

        :param colour_value: The RGB value to change this component to
        :return: None
        """
        self.image.fill(colour_value)

    def set_image(self, surface=None):
        """
        Sets this ui component to render a sprite instead of a rect

        :param surface: The pygame surface to draw
        :return: None
        """

        self.image = pg.Surface((0, 0))

        if surface is not None:
            self.original_image = surface.convert_alpha()
            self.image = self.original_image.copy()
            self.rect = self.image.get_rect()
            self.surface = surface

    def set_alpha(self, alpha_value):
        """
        Changes the alpha value of this component.

        :param alpha_value: 0 being fully transparent, 255 being completely visible
        :return: None
        """

        self.alpha_value = alpha_value
        self.image.set_alpha(alpha_value)

        if self.surface is not None:
            tmp = pg.Surface(self.rect.size, pg.SRCALPHA)
            tmp.fill((255, 255, 255, alpha_value))
            self.image = pg.transform.smoothscale(self.original_image, self.rect.size)
            self.image.blit(tmp, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    def set_parent(self, parent):
        """
        Sets the parent of this component.  This is used to add the component to a
        ui container.

        :param parent: The ui container to add this component to
        :return: None
        """
        self.parent_screen = parent
        parent.add_component(self)

    def set_visible(self, visibility=False):
        """
        Changes the visibility of this component

        :param visibility: Set to true to make this component visible
        :return: None
        """
        if visibility:
            UIMain.visible_ui_elements.add(self)
        else:
            UIMain.visible_ui_elements.remove(self)

    def set_tooltip(self, tooltip_component=None):
        """
        When this component is hovered over, a ui_element is displayed

        :param tooltip_component: A UIComponent or container that acts as the tooltip
        :return: None
        """
        self.tooltip = tooltip_component

    def on_click(self):
        """
        Event called when this component is clicked

        :return: None
        """
        self.is_clicking = True
        self.last_click_x = pg.mouse.get_pos()[0] - self.rect.x
        self.last_click_y = pg.mouse.get_pos()[1] - self.rect.y

        if self.click_event is not None:
            self.click_event()

    def on_release(self):
        """
        Event called when this components click is released

        :return: None
        """
        self.is_clicking = False
        if self.release_event is not None:
            self.release_event()

    def on_hover(self):
        """
        Event called when this component is moused over

        :return: None
        """
        if self.hovering_event is not None:
            self.hovering_event()

        if self.hover_event is not None and not self.hover:
            self.hover_event()

        self.hover = True

    def on_unhover(self):
        """
        Event called when the mouse is taken off this component

        :return: None
        """
        if self.unhover_event is not None:
            self.unhover_event()
