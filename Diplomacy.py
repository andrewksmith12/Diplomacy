from army import Army
locations_list = []
armies_list = []
support = {}

def add_one_to_support(army_name):
    """add one support to specified army name"""
    try: 
        support[army_name] += 1 
    except: 
        support[army_name] = 1 # If dictionary entry doesn't exist, create a dictionary entry. 

def read_line(s):
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
    if location not in locations_list:
        locations_list.append(location)
    army = Army(name, location, action)
    add_one_to_support(name) # add one to the support of this army. It supports itself!
    if action == "Move":
        army.action_move(location_or_supporting_army)
    if action == "Support":
        supporting_army_name = location_or_supporting_army 
        army.supporting(supporting_army_name) # add the name of the army that this army is supporting to a class variable. 
        add_one_to_support(supporting_army_name)
    armies_list.append(army)



# input 
def diplomacy_eval():
    # for army in armies_list:
    for army in armies_list:
        # for other armies:
        for other_army in armies_list:
            if not other_army == army:
                # if army action is support
                if army.action == "Support":
                    # if another_army destination is army.location (Army is being attacked)
                    if other_army.destination == army.location:
                        support[army.supporting] -= 1 #Remove one unit of support from the supporting army, they never arrive to help. 

                # if same destination
                if other_army.destination == army.location:
                    # compare total num of armies for that location
                    if support[army.name] == support[other_army.name]:
                        army.state = 0
                        other_army = 0
                    elif support[army.name] < support[other_army.name]:
                        army.state = 0
                    else:
                        other_army.state = 0


def diplomacy_print(w, army_name, location_or_dead):
    """
    w a writer
    """
    w.write(str(army_name) + " " + str(location_or_dead) + "\n")

        
def diplomacy_solve(r, w):
    for s in r:
        if not s.strip():  # Skips blank lines
            continue
        army_name, army_location, army_action, location_or_supporting_army = read_line(s)
        diplomacy_create_army(army_name, army_location, army_action, location_or_supporting_army)
        diplomacy_eval()
        for army in sorted(armies_list):
            if army.state == 0:
                diplomacy_print(w, army.name, "[dead]")
            else:
                diplomacy_print(w, army.name, army.location)
