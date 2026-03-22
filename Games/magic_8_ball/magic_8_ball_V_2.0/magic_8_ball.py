import random


class Magic8Ball:
    def __init__(self,response_file):
        responses_pool = []
        with open(response_file,"r") as r_file:
            for response in r_file:
                responses_pool.append(response)

        self.responses_pool = responses_pool

    def shake(self):
        return random.choice(self.responses_pool)
    




nod = Magic8Ball("responses.txt")


print(nod.shake())

    

    
        








