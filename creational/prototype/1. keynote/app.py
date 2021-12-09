from context_menu import ContextMenu
from circle import Circle


menu = ContextMenu()
circle = Circle()
circle.set_radius(12)
circle2 = menu.duplicate(circle)
print(circle2.get_radius())
circle2.render()