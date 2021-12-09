from component import Component


class ContextMenu:
    def duplicate(self, component: Component):
        return component.clone()