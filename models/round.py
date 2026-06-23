from datetime import datetime

class Round:

    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_datetime = datetime.now().isoformat()
        self.end_datetime = None

    def add_match(self, match):
        self.matches.append(match)

    def close(self):
        self.end_datetime = datetime.now().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": [match.to_dict() for match in self.matches],
        }

    def __repr__(self):
        return f"{self.name} ({len(self.matches)} matchs)"