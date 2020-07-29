import genix


class UISelectBox(genix.UIContainer):
    """
    A simple checkbox that can be bind to a boolean value
    """
    def __init__(self):
        super().__init__()

        self.switch = True

        self.click_event = self.switch_check
        self.add_constraint(genix.RelativeWidth(0.03))
        self.add_constraint(genix.HeightRatio())
        self.set_colour(genix.colours.DARK_GREY)

        self.select_box = genix.UIComponent()
        self.select_box.set_parent(self)
        self.select_box.set_colour(genix.colours.DARK_GREEN)
        self.select_box.add_constraint(genix.RelativeWidth(0.6))
        self.select_box.add_constraint(genix.HeightRatio())
        self.select_box.add_constraint(genix.CenterX())
        self.select_box.add_constraint(genix.CenterY())

    def switch_check(self, _switch=None):
        """
        Alternates the button's state of off and on

        :param _switch: Whether the switch should be on or off
        :return: None
        """
        if _switch is None:
            self.switch = not self.switch
            _switch = self.switch
        else:
            self.switch = None
        self.select_box.set_visible(_switch)