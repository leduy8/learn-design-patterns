from command import Command

class AddCustomerCommand(Command):
    def __init__(self, service) -> None:
        self.service = service

    def execute(self):
        self.service.add_customer()