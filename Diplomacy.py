support = {}
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
        return self.name < other.name


def add_one_to_support(army_name):
    """add one support to specified army name"""
    try: 
        support[army_name] += 1 
    except: 
        support[army_name] = 1 # If dictionary entry doesn't exist, create a dictionary entry. 

def diplomacy_read(s):
    """Split the army line into variables, pass these variables back to solve. """
    a = s.split()
    army_name = a[0]
    army_location = a[1]
    army_action = a[2]
    try:
        location_or_supporting_army = a[3]
        return army_name, army_location, army_action, location_or_supporting_army
    except IndexError:
        return army_name, army_location, army_action, ""
        
def diplomacy_create_army(name, location, action, location_or_supporting_army):
    """Take in variables from solve, create an army object to represent the army and it's actions. Append this variable to a list of armies."""
    army = Army(name, location, action)
    add_one_to_support(name) # add one to the support of this army. It supports itself!
    if action == "Move":
        army.action_move(location_or_supporting_army)
    if action == "Support":
        army.support(location_or_supporting_army) # add the name of the army that this army is supporting to a class variable. 
        add_one_to_support(location_or_supporting_army)
    return army

def diplomacy_eval(armies_list):
    """Determine if armies are supporting being attacked and/or supporting eachother. If armies is being attacked and supporting, remove the support. Then, cycle through all the battles and determine the winners. Update their properties accordingly. """
    battles_list = []
    # Determine if armies are supporting being attacked and/or supporting eachother. If an army is being attacked and supporting, remove the support. 
    for army in armies_list:
        for other_army in armies_list[armies_list.index(army)+1:]: 
            if other_army.destination == army.location:
                battles_list.append([army, other_army])
                if army.action == "Support":
                    support[army.supporting] -= 1 #Remove one unit of support from the supporting army, they never arrive to help. 
    
    # Cycle through the battles
    for armies in battles_list:
        # compare the support values for each battle, losers location to dead
        if support[armies[0].name] == support[armies[1].name]:
            armies[0].location = "[dead]"
            armies[1].location = "[dead]"
        elif support[armies[0].name] < support[armies[1].name]:
            armies[0].location = "[dead]"
        else:
            armies[1].location = "[dead]"
            
    # adjust moving armies destination to location
    for armies in armies_list:
        if armies.action == "Move" and armies.location != "[dead]":
            armies.location = armies.destination
            
    return armies_list


def diplomacy_print(w, army_name, location_or_dead):
    """
    Format and write the output to w. 
    """
    w.write(str(army_name) + " " + str(location_or_dead) + "\n")

        
def diplomacy_solve(r, w):
    """Process Input, create armies, solve for armies actions. Call functions to solve the diplomacy problem."""
    armies_list = []
    reset_support()
    for s in r:
        if not s.strip():  # Skips blank lines
            continue
        army_name, army_location, army_action, location_or_supporting_army = diplomacy_read(s)
        armies_list.append(diplomacy_create_army(army_name, army_location, army_action, location_or_supporting_army))
    armies_list = diplomacy_eval(armies_list)
    for army in armies_list:
        diplomacy_print(w, army.name, army.location)

def reset_support():
    support.clear()