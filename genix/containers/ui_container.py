import genix


class UIContainer(genix.UIComponent):
    """
    A storage for different ui components, derived from UIComponent.

    Its children are contained within the components list
    """
    def __init__(self):
        super().__init__()
        self.components = []
        self.name = ""

    def add_component(self, component):
        """
        Acts as a variation to set_parent()

        :param component: The component to add
        :return: None
        """
        self.components.append(component)

    def add_x(self, transform_value=0):
        """
        Overrides UIComponent add_x by changing the x values of itself and it's children

        :param transform_value: Amount to transform x by
        :return: None
        """
        self.rect.x += transform_value

        for component in self.__get_components():
            component.add_x(transform_value)

    def add_y(self, transform_value=0):
        """
        Overrides UIComponent add_y by changing the y values of itself and its children

        :param transform_value: Amount to transform y by
        :return: None
        """
        self.rect.y += transform_value

        for component in self.__get_components():
            component.add_y(transform_value)

    def __get_components(self):
        """
        Builds a list of each separate component of this ui container

        :return: A built list of this UIContainers components
        """
        build_components = []

        for ui_component in self.components:
            build_components.append(ui_component)
            # if hasattr(ui_component, 'components'):
            #     self.__breakdown_component(ui_component.components)

        return build_components

    def __breakdown_component(self, component):
        """
        Called recursively and used to break down each ui container into its individual components

        :param component: The list that contains the ui components
        :return: None
        """
        for ui_component in component:
            if hasattr(ui_component, 'components'):
                self.__breakdown_component(ui_component)
            else:
                component.append(ui_component)
                break
