import random

class Magic_8_Ball:
    def __init__(self,response_pool):
        self.response_pool = response_pool

    def shake(self):
        
        return ("Magic 8 Ball:",random.choice(self.response_pool)

    
        


class game_program:
    def __init__(self,magic_8_ball,question):
        self.magic_8_ball = magic_8_ball
        self.question = question


    def ask_question(self):
        print("User Question:",self.question)
        print(self.magic_8_ball.shake())





game = game_program(Magic
