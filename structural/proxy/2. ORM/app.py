from db_context import DbContext

db_context = DbContext()
product = db_context.get_product(1)

product.set_name("Updated Name")
db_context.save_changes()

product.set_name("Another name")
db_context.save_changes()