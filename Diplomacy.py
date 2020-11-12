from army import Army
support = {}


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
        supporting_army_name = location_or_supporting_army 
        army.support(supporting_army_name) # add the name of the army that this army is supporting to a class variable. 
        add_one_to_support(supporting_army_name)
    return army



def diplomacy_eval(armies_list):
    battles_list = []
    # Determine if armies are supporting being attacked and/or supporting eachother. If armies is being attacked and supporting, remove the support. 
    for army in armies_list:
        for other_army in armies_list[armies_list.index(army)+1:]: 
            if other_army.destination == army.location:
                battles_list.append([army, other_army])
                if army.action == "Support":
                    support[army.supporting] -= 1 #Remove one unit of support from the supporting army, they never arrive to help. 
                # if same destination
    
    # Cycle through the battles
    for armies in battles_list:
        # compare total num of armies for that location
        #print("Battle Initated: ")
        #print("Support: "+str(armies[0].name)+": "+str(support[armies[0].name]))
        #print("Support: "+str(armies[1].name)+": "+str(support[armies[1].name]))

        if support[armies[0].name] == support[armies[1].name]:
            armies[0].location = "[dead]"
            armies[1].location = "[dead]"
        elif support[armies[0].name] < support[armies[1].name]:
            armies[0].location = "[dead]"
        else:
            armies[1].location = "[dead]"

    # action = "Move" -> destination to location
    for armies in armies_list:
        if armies.action == "Move" and armies.location != "[dead]":
            armies.location = armies.destination
            
    return armies_list


def diplomacy_print(w, army_name, location_or_dead):
    """
    w a writer
    """
    w.write(str(army_name) + " " + str(location_or_dead) + "\n")

        
def diplomacy_solve(r, w):
    armies_list = []
    support.clear()
    for s in r:
        if not s.strip():  # Skips blank lines
            continue
        army_name, army_location, army_action, location_or_supporting_army = diplomacy_read(s)
        armies_list.append(diplomacy_create_army(army_name, army_location, army_action, location_or_supporting_army))
    armies_list = diplomacy_eval(armies_list)
    for army in armies_list:
        diplomacy_print(w, army.name, army.location)
