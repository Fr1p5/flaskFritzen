class player:

    amount_players = 0
    raise_points = input("Enter points: ")

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def score(self):
        self.points = int(self.points + self.raise_points)