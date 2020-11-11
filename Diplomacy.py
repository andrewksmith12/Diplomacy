from army import Army
locations_list = []
armies_list = []
support = {}

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
    if action == "Move":
        army.action_move(location_or_supporting_army)
    if action == "Support":
        supporting_army = location_or_supporting_army
        # 
        try:
            support[supporting_army] += 1
        except:
            support[supporting_army] = 1
    armies_list.append(army)


# input 
def diplomacy_eval():
    # for army in armies_list:
    for army in armies_list:
        # get location
        location = army.location
        # for other armies:
        for other_army in armies_list:
            if not other_army == army:
                # if army action is support
                    # if another_army destination is army.location
                        # army.state = 0
                        # -1 from dictionary

                # if same destination
                if other_army.destination == army.location:
                    # compare total num of armies for that location
                    if support[army.name] == support[other_army.name]:
                        army.state = 0
                        other_army = 0
                    elif support[army.name] < support[other_army.name]:
                        army.state = 0
                    else:
                        army.state = 0


    #AKS
    # If an army is being attacked, it can't support.
        #Insert loop that checks for fighting armies and invalidates their support. 
    # Then, compare support for attacks and update status of losers. 
    return ""



        
def diplomacy_solve(r, w):
    for s in r:
        if not s.strip():  # Skips blank lines
            continue
        army_name, army_location, army_action, location_or_supporting_army = read_line(s)
        diplomacy_create_army(army_name, army_location, army_action, location_or_supporting_army)

    #diplomacy_eval()
    #diplomacy_print()
