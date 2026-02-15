#My database function that houses all of the lists that I need
def init_database(): 
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = ["1", "2", "3", "4", "5"]
    #allows main to use all 4 of my lists in paralell
    return names, ranks, divs, ids 

def display_menu():
    #ask user name for future use, as well as removing empty spaces and capitlising it
    user_name = input("Please enter your full name:").strip().title()
    #List of menu options to use later
    valid_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        print("<<< FLEET MANAGER MENU >>>")
        print("Currently logged in as:", user_name) #Ask for users name, then display it for them

        print("1. Display current crew")
        print("2. Add member")
        print("3. Remove member")
        print("4. Update rank")
        print("5. Search crew")
        print("6. Filter by division")
        print("7. Calculate payroll")
        print("8. Count officers")
        print("9. Exit")
        #Displays the list of options and then asks to select an option
        #This is all in a while loop so that if the user enters anything except the desired input
        #We will loop infinitely until they do
        option = input("Select an option (1-9):").strip()

        if option in valid_options:
            return option
        #Checks if the user selects the correct input, otherwise the else statement triggers and we loop
        else:
            print("\n INVALID OPTION CHOSEN. \n") #The spacers just make it pretty in my opinion

def add_member(names, ranks, divs, ids):
    new_name = input("Enter crew name:").strip().title()
    #Simple input for a new name

    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    while True:
        print("Valid ranks are:", valid_ranks)
        new_rank = input("Enter crew rank:").strip().title()
        if new_rank in valid_ranks:
            break
        else:
            print("ERROR: Invalid Rank.")
            #Tells you what the ranks are, checks if you enter the right one and will loop until you do

    valid_divs = ["Command", "Operations", "Sciences"]
    while True:
        print("Valid divisions are:", valid_divs)
        new_div = input("Enter crew division:").strip().title()
        #Same loop, but for divisions
        if new_div in valid_divs:
            break
        else:
            print("ERROR: Invalid Division")
    
    while True:
        new_id = input("Enter crew id:").strip()

        if new_id in ids:
            print("ERROR: ID already exists")
        else:
            break
            #Same loop, but for IDS
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    #Updates all 4 lists with the infomformation gathered, making sure they stay in parallel
    print("Crew member added")

def remove_member(names, ranks, divs, ids):
    rem_id = input("Enter crew ID to remove:").strip()

    if rem_id in ids:
        index = ids.index(rem_id)
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("Crew member removed.")
    else:
        print("ERROR: ID not found.")

def main(): #function for the main program that utilises my 10 base functions
    names, ranks, divs, ids = init_database() #calling the variable and stores the lists
    print("Database initialised.") #mostly a diagnostic tool really, but looks cool

    
    
    option = display_menu()
    if option == "1":
        print ("Display crew selected")

    elif option == "2":
        add_member(names, ranks, divs, ids)
        for i in range(len(names)): #just literally testing if my lists work, will remove later
            print(names[i], ranks[i], divs[i], ids[i])

    elif option == "3":
        remove_member(names, ranks, divs, ids)
        for i in range(len(names)):
            print(names[i], ranks[i], divs[i], ids[i])
main()
