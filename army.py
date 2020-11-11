class Army:
    def __init__(self, name, location, action):
        self.name = name
        self.action = action
        self.location = location
        self.destination = ""
        self.supporting = ""
        self.state = 1

    def update_result(self, state):
        self.state = state

    def action_move(self, destination):
        self.destination = destination

    def support(self, supporting):
        self.supporting = supporting
