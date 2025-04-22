from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing Diamond Trap."""

    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def set_eyes(self, e):
        self.eyes = e

    def set_hairs(self, h):
        self.hairs = h

    def __str__(self):
        """Overriding __str__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Overriding __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
