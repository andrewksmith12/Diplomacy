class Army:
    def __init__(self, name, action, location, supporting=[]):
        self.name = name
        self.action = action
        self.location = location
        self.supporting = supporting
        self.state = 1
    def support(self, armies, name, location):
        self.action="Supporting"
        self.locaton = location
        armies.name.supporting.append(self)
    def hold(self):
        self.action="Hold"
    def move(self, location):
        self.location = location
    def store_result(self, state):
        self.state = state
