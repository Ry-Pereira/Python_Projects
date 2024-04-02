import random

class Magic_8_Ball:
    def __init__(self,response_pool):
        self.response_pool = response_pool

    def shake(self):
        return ("Magic 8 Ball:",random.choice(self.response_pool))

    
        








