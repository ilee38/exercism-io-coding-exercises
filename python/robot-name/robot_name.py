import random

class Robot(object):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.name = self._get_rand_name()


    def _get_rand_name(self):
        """ Return name of the form: "AB123"
        """
        random.seed()
        A = self.alpha[random.randint(0, 26)]
        B = self.alpha[random.randint(0,26)]
        n1 = str(random.randint(0,9))
        n2 = str(random.randint(0,9))
        n3 = str(random.randint(0,9))
        return "{}{}{}{}{}".format(A,B,n1,n2,n3)

    def reset(self):
        self.name = self._get_rand_name()
