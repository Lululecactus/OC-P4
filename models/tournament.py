class Tournament:
    
    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = description

    def add_player(self, player):
        self.players.append(player)

    def is_finished(self):
        return self.current_round >= self.number_of_rounds

    def generate_round_pairs_random(self):
        pass
# 1. Mélanger les joueurs de manière aléatoire
# 2. Les associer par paires
# 3. S'il y a un nombre impair de joueurs, le dernier joueur ne sera pas associé
# 4. Retourner la liste des paires  