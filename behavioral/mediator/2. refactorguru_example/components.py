from base_component import BaseComponent

# * Note: I'm just lazy

class Component1(BaseComponent):
    def do_a(self):
        print('Component 1 does A')
        self.mediator.notify(self, "A")

    def do_b(self):
        print('Component 1 does B')
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self):
        print('Component 2 does C')
        self.mediator.notify(self, "C")

    def do_d(self):
        print('Component 2 does D')
        self.mediator.notify(self, "D")