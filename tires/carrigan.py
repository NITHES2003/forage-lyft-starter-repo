from tires.tires import tire

class CarriganTire(tire):
    def __init__(self, array):
        self.array = array        

    def needs_service(self):
        for i in self.array:
            if i >= 0.9:
                return True
        return False
            