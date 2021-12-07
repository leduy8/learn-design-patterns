from product_proxy import ProductProxy

class DbContext:
    def __init__(self) -> None:
        self.update_objects = {}

    def get_product(self, id):
        # * Automatically generate SQL statements
        # * to read the product with the given ID.
        print(f'SELECT * FROM products WHERE product_id = {id}')

        product = ProductProxy(id, self)
        product.set_name("Product 1")

        return product

    def save_changes(self):
        # * Automatically generate SQL statements
        # * to update the database.
        for update_obj in self.update_objects.values():
            print(f'UPDATE products SET name = {update_obj.get_name()} WHERE product_id = {update_obj.get_id()}')

        self.update_objects.clear()

    def mark_as_changed(self, product: ProductProxy):
        self.update_objects[product.get_id()] = product