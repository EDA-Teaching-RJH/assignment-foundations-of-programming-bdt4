def init_database(): #My database function that houses all of the lists that I need
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["1", "2", "3", "4", "5"]
    return names, ranks, divs, ids #allows main to use all 4 of my lists
def main(): #function for the main program that utilises my 10 base functions
    names, ranks, divs, ids = init_database() #calling the variable and stores the lists
    print("Database initialised.") #mostly a diagnostic tool really, but looks cool
    for i in range(len(names)): #just literally testing if my lists work, will remove later
        print(names[i], ranks[i], divs[i], ids[i])
main()
