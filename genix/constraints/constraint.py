class Constraint:
    def __init__(self):
        self.priority = 0

    def update_constraint(self, ui_element=None):
        """
        Every constraint subclass shadows this method

        :param ui_element: The UI element to modify
        :return:
        """
