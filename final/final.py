# Program that aids in a soccer team's tryout process
# by taking in a list of players and their stats
# to find the best player.

# ASSUMPTIONS: Program assumes that no two players are of
# equal skill, that user follows directions properly, (inputs what the programs asks for)
# that the user uses integers, and that all players are strikers.

def main():
    # Asks how many strikers are trying out
    s = input("How manys strikers are trying out?: ")
    s = int(s)
    # Ends program if user if given only one or less players
    if s <= 1:
        print("Please provide at least 2 or more players")
        exit()

    # Asks for, and saves striker names in a list using append
    striker_name = []
    for i in range(s):
        name = input("Striker name: ")
        striker_name.append(name)

    # Calls functions that determine a striker's stats
    acc = accuracy_finder(s, striker_name)
    drr = dribble_finder(s, striker_name)
    pss = pass_finder(s, striker_name)
    ovr = ovr_calculator(s, acc, drr, pss)

    # Compares player Overalls and finds best player
    spot = 0
    great = max(ovr)

    # Determines which player is the best
    for i in range(s):
        if ovr[i] == great:
            spot = i
            break
    spot = int(spot)

    # Prints who the best player is
    print(f"Best Striker is {striker_name[spot]}, with an Overall of {ovr[spot]}!")

# Finds the accuracy of each player
def accuracy_finder(s, striker_name):

    # Asks for striker's shot accuracy and saves in a list
    striker_accuracy = []
    for i in range(s):
        shots = input(f"{striker_name[i]} How many shots taken?: ")
        shots = int(shots)
        # Re-prompts user if given innacurate information
        if shots < 0:
            print("Please provide accurate information.")
            exit()
        target = input(f"{striker_name[i]} How many shots on target?: ")
        target = int(target)
        if target > shots or target < 0:
            print("Please provide accurate information.")
            exit()
        accuracy = target / shots
        accuracy = accuracy * 100
        striker_accuracy.append(accuracy)
    return striker_accuracy

# Finds the dribble success rate of each player
def dribble_finder(s, striker_name):
    # Asks for striker's dribbling success rate and saves in a list
    striker_dribble_rate = []
    for i in range(s):
        dribbles = input(f"{striker_name[i]} How many dribbles done?: ")
        dribbles = int(dribbles)
        # Re-prompts user if given innacurate information
        if dribbles < 0:
            print("Please provide accurate information.")
            exit()
        successful = input(f"{striker_name[i]} How many were successful?: ")
        successful = int(successful)
        if successful > dribbles or successful < 0:
            print("Please provide accurate information.")
            exit()
        rate = successful / dribbles
        rate = rate * 100
        striker_dribble_rate.append(rate)
    return striker_dribble_rate

# Finds the pass success rate of each player
def pass_finder(s, striker_name):

    # Asks for striker's passing success rate and saves in a list
    striker_pass_rate = []
    for i in range(s):
        passes = input(f"{striker_name[i]} How many passes made?: ")
        passes = int(passes)
        # Re-prompts user if given innacurate information
        if passes < 0:
            print("Please provide accurate information.")
            exit()
        through = input(f"{striker_name[i]} How many were received?: ")
        through = int(through)
        if through > passes or through < 0:
            print("Please provide accurate information.")
            exit()
        vision = through / passes
        vision = vision * 100
        striker_pass_rate.append(vision)
    return striker_pass_rate

# Calculates a player's Overall stat
def ovr_calculator(s, acc, drr, pss):

    # Calculates player's Overall Rating using their stat averages and saves in a list
    striker_ovr = []
    for i in range(s):
        ovr = 0
        ovr = ((acc[i] + drr[i] + pss[i]) / 3)
        ovr = int(ovr)
        striker_ovr.append(ovr)
    return striker_ovr

main()