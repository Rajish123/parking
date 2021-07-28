


class Vechile:
    def __init__(self, catagoery, model, registration_num, colour):
        self.catagoery = catagoery
        self.model = model
        self.registration_num = registration_num
        self.colour = colour

    def __str__(self):
        return f"Catagoery: {self.catagoery}\n Model: {self.model}\n Registration number:{self.registration_num}\n Colour:{self.colour}"