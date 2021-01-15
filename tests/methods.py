class player:

    amount_players = 0
    raise_points = input("Enter points: ")

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def score(self):
        self.points = int(self.points + self.raise_points)

    print(raise_points)

names = ['user1', 'user2', 'user3']
points = [420, 69, 120]

scoreBoard = list(zip(names, points))

print(scoreBoard)

for x in scoreBoard:
    print('{} has {} points'.format(x[0], x[1]))
