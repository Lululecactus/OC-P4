class Player:
   
    def __init__(self, last_name, first_name, birth_date, chess_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.points = 0.0

    def add_points(self, amount):
        self.points += amount

    def to_dict(self):
    # Object -> JSON
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "points": self.points,
        }

    @classmethod
    def from_dict(cls, data):
    # JSON -> Object
        player = cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["chess_id"],
        )
        player.points = data.get("points", 0.0)
        return player

    def __repr__(self):
    # Définit ce qui s'affiche quand on fait print player.
        return (
            f"{self.first_name} {self.last_name} "
            f"({self.chess_id}) - {self.points} pts"
        )