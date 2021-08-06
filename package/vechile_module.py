


class Vechile:
    def __init__(self, catagoery, model, registration_num, colour):
        self.catagoery = catagoery
        self.model = model
        self.registration_num = registration_num
        self.colour = colour

    def display_info(self):
        return self.catagoery,self.model,self.registration_num,self.colour