from tires.tires import tire

class CarriganTire(tire):
    def __init__(self, array):
        self.array = array
        

    def needs_service(self):
        return sum(self.array)>=3
            