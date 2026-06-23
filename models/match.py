class Match:
    
    def __init__(self, player1, player2):
        self.data = ([player1, 0.0], [player2, 0.0])

    def set_result(self, result):
    
        if result == 1:
            self.data[0][1] = 1.0
            self.data[1][1] = 0.0
        elif result == 2:
            self.data[0][1] = 0.0
            self.data[1][1] = 1.0
        else:
            self.data[0][1] = 0.5
            self.data[1][1] = 0.5

        self.data[0][0].add_points(self.data[0][1])
        self.data[1][0].add_points(self.data[1][1])

    def to_dict(self):
        return [
            [self.data[0][0].national_id, self.data[0][1]],
            [self.data[1][0].national_id, self.data[1][1]],
        ]

    def __repr__(self):
        player1, score1 = self.data[0]
        player2, score2 = self.data[1]
        return f"{player1.first_name} ({score1}) vs {player2.first_name} ({score2})"