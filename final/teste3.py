# Program serves as a tool to help the tryout process
# by taking in player names and stats and returning
# the best player.
# Assumes there are not players of equal skill

def main():
    # Asks how many strikers are trying out
    s = input("How manys strikers are trying out?: ")
    s = int(s)
    if s == 1:
        print("They are the best!")
        exit()
    if s <= 0:
        print("Then why use program?.")
        exit()

    # Asks for and saves striker names in a list
    striker_name = []
    for i in range(s):
        name = input("Striker name: ")
        striker_name.append(name)

    acc = accuracy_finder(s, striker_name)
    drr = dribble_success_rate_finder(s, striker_name)
    pss = pass_success_rate_finder(s, striker_name)

    # Calculates player's Overall Rating using their stat averages and saves in a list
    striker_ovr = []
    for i in range(s):
        ovr = 0
        ovr = ((acc[i] + drr[i] + pss[i]) / 3)
        ovr = int(ovr)
        striker_ovr.append(ovr)

    print(f"{striker_name}")
    print(f"{striker_acc}")
    print(f"{striker_drr}")
    print(f"{striker_pss}")
    print(f"{striker_ovr}")


    # Compares player Overalls and finds best player
    spot = 0
    great = max(striker_ovr)

    for i in range(striker_ovr[i]):
        if striker_ovr[i] == great:
            spot = i
            break
    spot = int(spot)

    # Prints who the best player is
    print(f"Best Striker is {striker_name[spot]}")

def accuracy_finder(s, striker_name):

    # Asks for striker's shot accuracy and saves in a list
    striker_accuracy = []
    for i in range(s):
        shots = input(f"{striker_name[i]} How many shots taken?: ")
        shots = int(shots)
        target = input(f"{striker_name[i]} How many shots on target?: ")
        target = int(target)
        if target > shots:
            print("Please provide accurate information.")
            exit()
        accuracy = target / shots
        accuracy = accuracy * 100
        striker_accuracy.append(accuracy)
    return striker_accuracy


def dribble_success_rate_finder(s, striker_name):

    # Asks for striker's dribbling success rate and saves in a list
    striker_dribble_rate = []
    for i in range(s):
        dribbles = input(f"{striker_name[i]} How many dribbles done?: ")
        dribbles = int(dribbles)
        successful = input(f"{striker_name[i]} How many were successful?: ")
        successful = int(successful)
        if successful > dribbles:
            print("Please provide accurate information.")
            exit()
        rate = successful / dribbles
        rate = rate * 100
        striker_dribble_rate.append(rate)
    return striker_dribble_rate

def pass_success_rate_finder(s, striker_name):

    # Asks for striker's passing success rate and saves in a list
    striker_pass_rate = []
    for i in range(s):
        passes = input(f"{striker_name[i]} How many passes made?: ")
        passes = int(passes)
        through = input(f"{striker_name[i]} How many were received?: ")
        through = int(through)
        if through > passes:
            print("Please provide accurate information.")
            exit()
        vision = through / passes
        vision = vision * 100
        striker_pass_rate.append(vision)

#def ovr_calculator():


main()