from product import Product


class ProductProxy(Product):
    def __init__(self, id, context) -> None:
        super().__init__(id)
        self.context = context

    def set_name(self, name):
        super().set_name(name)

        self.context.mark_as_changed(self)