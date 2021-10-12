import random

# TODO: Define the Hider class here

class Hider:
    '''
    The responsibility of the class is to hide from the seeker
    and give hints about the hiders location

    Stereotype:
        Information holder

    Attributes:
        location (integer): location of the hider
        distance (list): The distance travelled with each move.
    '''

    def __init__(self):
        '''Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        '''

        self.location = random.randint(1,1000)
        self.distance = [0, 0] # start with two so get_hint always works
        print( self.location )

    def watch(self, location):
        '''keeps track of how far away the seeker is by
        calculating the difference between their locations.
        The distance is appended to the corresponding attribute for later use. 
        '''
        distance = abs(self.location - location)
        self.distance.append(distance)
    

    def get_hint(self):
        '''returns a hint that depends on whether or not the seeker has moved closer or farther away.
        This is determined by inspecting the last two distances contained in the distance attribute.
        '''

        hint = "(^.^) You won't find me!"

        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"

        return hint