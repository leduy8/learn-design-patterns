class ContextMenu:
    def __init__(self, timeline) -> None:
        self.timeline = timeline

    def duplicate(self, component):
        clone = component.clone()
        self.timeline.add(clone)