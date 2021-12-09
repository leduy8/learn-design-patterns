from controller import Controller
from sharp_controller import SharpController


class ProductsController(SharpController):
    def list_products(self):
        # get products from db...
        context = {}
        # add new product to context...
        self.render("products.html", context)