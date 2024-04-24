class MemoryCard:

    def __init__(self,top_side,bottom_side):
        self.top_side = top_side
        self.bottom_side = bottom_side



    def __str__(self):
        return self.top_side + ":" + self.bottom_side
