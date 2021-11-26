from observer import Observer


class Chart(Observer):
    def update(self, value):
        print(f'Chart got updated: {value}')