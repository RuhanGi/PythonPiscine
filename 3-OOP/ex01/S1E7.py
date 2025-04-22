from S1E9 import Character


class Baratheon(Character):
    """Your docstring for Class"""
   def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        Character.__init__(self, name, is_alive)

    def __str__(self):
        return f"{self.name}({self.is_alive})"

    def __repr__(self):
        return f"{self.name}({self.is_alive})"

class Lannister(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        Character.__init__(self, name, is_alive)

    def __str__(self):
        return f"{self.name}({self.is_alive})"

    def __repr__(self):
        return f"{self.name}({self.is_alive})"
    
        # decorator
    def create_lannister(your code here):
        #your code here