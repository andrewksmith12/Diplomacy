class Army:
    def __init__(self, name, location, action):
        self.name = name
        self.action = action
        self.location = location
        self.destination = ""
        self.supporting = ""

    def action_move(self, destination):
        self.destination = destination

    def support(self, supporting):
        self.supporting = supporting

    def __lt__(self, other):
        return self.name < other.name #PRAGMA: no cover
