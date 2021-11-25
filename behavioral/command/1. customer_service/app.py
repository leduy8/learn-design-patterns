from customer_service import CustomerService
from add_customer_command import AddCustomerCommand
from button import Button

service = CustomerService()
command = AddCustomerCommand(service)
button = Button(command)
button.click()
