import pygame as pg
import genix

pg.init()

win = genix.UIWindow()
win.set_title("Backpack Genix Example")

genix_main = genix.UIMain(win)

clock = pg.time.Clock()


class TabTooltip(genix.UIContainer):
    def __init__(self, name=""):
        super().__init__()

        self.add_constraint(genix.RelativeWidth(0.3))
        self.add_constraint(genix.RelativeHeight(0.075))
        self.set_colour(genix.colours.DARK_GREY)

        self.label = genix.UIText(name)
        self.label.set_size(20)
        self.label.set_parent(self)
        self.label.set_font("28 days later")
        self.label.add_constraint(genix.Centered())


class Tab(genix.UIContainer):
    def __init__(self, name=""):
        super().__init__()

        self.add_constraint(genix.RelativeWidth(0.2))
        self.add_constraint(genix.RelativeHeight(0.075))
        self.set_colour(genix.colours.BLOOD_RED)

        self.label = genix.UIText(name)
        self.label.set_size(25)
        self.label.set_parent(self)
        self.label.set_font("28 days later")
        self.label.add_constraint(genix.Centered())

        self.click_event = self.click_slot
        self.hover_event = self.hover_slot
        self.unhover_event = self.unhover_slot
        self.release_event = self.unclick_slot

    def click_slot(self):
        self.set_colour(genix.colours.RED)

    def unclick_slot(self):
        self.set_colour(genix.colours.DARK_RED)

    def hover_slot(self):
        self.set_colour(genix.colours.DARK_RED)

    def unhover_slot(self):
        self.set_colour(genix.colours.BLOOD_RED)


box = genix.UIContainer()
box.add_constraint(genix.RelativeWidth(0.25))
box.add_constraint(genix.RelativeHeight(0.6))
box.add_constraint(genix.Centered())
box.set_alpha(150)
box.set_move(True)

text = genix.UIText("Backpack")
text.set_font("28 days later")
text.set_parent(box)
text.set_size(50)
text.add_constraint(genix.CenterX())
text.add_constraint(genix.Vertical(0.05))

top_line = genix.UIComponent()
top_line.set_parent(box)
top_line.set_colour(genix.colours.BLOOD_RED)
top_line.add_constraint(genix.RelativeWidth(0.8))
top_line.add_constraint(genix.RelativeHeight(0.008))
top_line.add_constraint(genix.CenterX())
top_line.add_constraint(genix.Vertical(0.18))

grid = genix.UIGrid()
grid.set_parent(box)
grid.set_spacing(y_spacing=0.15)
grid.set_columns(3)
grid.add_constraint(genix.CenterY())
grid.add_constraint(genix.Horizontal(0.05))

weapons = Tab("Weapons")
weapons.set_parent(grid)

tools = Tab("Tools")
tools.set_parent(grid)

apparel = Tab("Apparel")
apparel.set_parent(grid)

weapon_tooltip = TabTooltip("Your weapons")
weapon_tooltip.set_parent(box)
weapons.set_tooltip(weapon_tooltip)

tools_tooltip = TabTooltip("Your tools")
tools_tooltip.set_parent(box)
tools.set_tooltip(tools_tooltip)

apparel_tooltip = TabTooltip("Your apparel")
apparel_tooltip.set_parent(box)
apparel.set_tooltip(apparel_tooltip)


run = True
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        genix_main.do_events(event)

    clock.tick(60)

    win.screen.fill((0, 150, 0))

    genix_main.main()

    pg.display.update()

pg.quit()
