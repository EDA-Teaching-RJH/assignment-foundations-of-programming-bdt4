#My database function that houses all of the lists that I need
def init_database(): 
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = ["1", "2", "3", "4", "5"]
    #allows main to use all 4 of my lists in paralell
    return names, ranks, divs, ids 

def display_menu(user_name):
    #List of menu options to use later
    valid_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        print("\n<<< FLEET MANAGER MENU >>>")
        print("Currently logged in as: ", user_name) #Ask for users name, then display it for them

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
        option = input("\nSelect an option (1-9): ").strip()

        if option in valid_options:
            return option
        #Checks if the user selects the correct input, otherwise the else statement triggers and we loop
        else:
            print("\n INVALID OPTION CHOSEN. \n") #The spacers just make it pretty in my opinion

def add_member(names, ranks, divs, ids, valid_ranks, valid_divs):
    new_name = input("Enter crew name: ").strip().title()
    #Simple ask for a new name

    while True:
        print("Valid ranks are", valid_ranks)
        new_rank = input("Enter crew rank: ").strip().title()
        if new_rank in valid_ranks:
            break
        else:
            print("ERROR: Invalid Rank.")
            #Tells you what the ranks are, checks if you enter the right one and will loop until you do

    while True:
        print("Valid divisions are: ", valid_divs)
        new_div = input("Enter crew division: ").strip().title()
        #Same loop, but for divisions
        if new_div in valid_divs:
            break
        else:
            print("ERROR: Invalid Division")
    
    while True:
        new_id = input("Enter crew id: ").strip()

        if new_id in ids:
            print("ERROR: ID already exists")
        else:
            break
            #Same loop, but for IDS
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    #Updates all 4 lists with the information gathered, making sure they stay in parallel

    print("\n Crew member added:")
    print("ID:", new_id)
    print("Name:", new_name)
    print("Rank:", new_rank)
    print("Division:", new_div)
    #prints out the information of the person added

def remove_member(names, ranks, divs, ids):
    while True: #Same loop as before, we just go until correct input is presented and then continue once it is
        rem_id = input("Enter crew ID to remove: ").strip()
        #Checks if the ID is in the list of ids and if it is, deletes it
        if rem_id in ids:

            index = ids.index(rem_id)
            print("\nRemoving crew member:")
            print("ID:", ids[index])
            print("Name:", names[index])
            print("Rank:", ranks[index])
            print("Division:", divs[index])
            #Show the details of the person being removed

            names.pop(index)
            ranks.pop(index)
            divs.pop(index)
            ids.pop(index)
            #Remove the details from parallel lists
            print("Crew member removed.")
            break
        else:
            print("ERROR: ID not found.")
            #Otherwise spits an error out

def update_rank(names, ranks, ids, valid_ranks):
    while True:
        target_id = input("\nEnter crew ID to update: ").strip()

        if target_id in ids:
            index = ids.index(target_id)
            break
        else:
            print("ERROR: ID not found.")
        
    print("Crew member: ", names[index])
    print("Current rank: ", ranks[index])
    
    while True:
        print("Valid ranks are: ", valid_ranks)
        new_rank = input("Enter new rank: ").strip().title()

        if new_rank in valid_ranks:
            ranks[index] = new_rank
            print("Rank updated to: ", ranks[index])
            break
        else:
            print("ERROR: Invalid Rank")
            #Searches through ids, verifies if id exists and then asks for rank, verifies again and updates

def display_roster(names, ranks, divs, ids):
    print("\n <<<CURRENT CREW ROSTER >>>")
    
    if len(names) == 0:
        print("Roster is empty.")
        return
    #Just in case roster is empty so that things don't break
    
    #calculutes automatic width for columns
    #found a cool way to do this automatically rather than doing it manually, I do realise this may
    #cause issues if people want to make stupidly long names but this visual makes my brain happy
    id_width = max(len("ID"), max(len(crew_id) for crew_id in ids))
    name_width = max(len("Name"), max(len(crew_name) for crew_name in names))
    rank_width = max(len("Rank"), max(len(crew_rank) for crew_rank in ranks))
    div_width = max(len("Division"), max(len(crew_div) for crew_div in divs))

    
    print(f"{'ID':<{id_width}} | {'Name':<{name_width}} | {'Rank':<{rank_width}} | {'Division':<{div_width}}")
    #print header
    
    
    total_width = id_width + name_width + rank_width + div_width + 9
    print("-" * total_width)
    #print the seperator line

    
    for i in range(len(names)):
        print(f"{ids[i]:<{id_width}} | {names[i]:<{name_width}} | {ranks[i]:<{rank_width}} | {divs[i]:<{div_width}}")
    #print rows

def search_crew(names, ranks, divs, ids):
    search_name = input("Enter a name to search: ").strip().lower()
    #input a search and make it all lowercase coming out so that it doesn't cause issues
    found = False

    for i in range(len(names)):
        if search_name in names[i].lower(): #we are searching lowercase so no issues occur
            print("\nMatch found: ")
            print("ID: ", ids[i])
            print("Name: ", names[i])
            print("Rank: ", ranks[i])
            print("Division: ", divs[i])
            found = True
            #prints out the information found, or if not found, that it couldn't find it
    if found == False:
        print("No matching crew members found.")

def filter_by_division(names, ranks, divs, ids, valid_divs):
    while True:
        print("Valid divisions are: ", valid_divs)
        target_div = input("Enter division to filter by: ").strip().title()
        #Asks for which division to search by, while also giving correct divisions
        if target_div in valid_divs:
            break
        else:
            print("ERROR: Invalid Division")
    print("\nCrew members in", target_div, "division:")
    #If the division is found in the list, continue, if not, print an error and keep going
    found = False

    for i in range(len(names)):
        if divs[i] == target_div:
            print("ID:", ids[i])
            print("Name:", names[i])
            print("Rank:", ranks[i])
            print("Division:", divs[i])
            print() #Just incase multiple are found so we seperate by one line
            found = True
            #When a division is chosen, print out information of those in that division
    if found == False:
        print("No crew members found in that division.")

def calculate_payroll(ranks):
    pay_rates = {"Captain": 1000, "Commander": 800, "Lt. Commander": 600, "Lieutenant": 400, "Ensign": 200}
    #using the dictionary feature of python to assign a number value to the ranks in the list
    total = 0 #set it to 0 so that only the ranks cause the numbe to go up or down

    for rank in ranks:
        total = total + pay_rates[rank]

    return total
    #simple for loop to automatically adjust the payrates when crew members are added, deleted or otherwise
    
def main(): #function for the main program that utilises my 10 base functions
    names, ranks, divs, ids = init_database() #calling the variable and stores the lists
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    valid_divs = ["Command", "Operations", "Sciences"]
    print("Please wait...")
    print("Database initialised.") #mostly a diagnostic tool really, but looks cool

    #ask user name for future use, as well as removing empty spaces and capitalising it
    user_name = input("Please enter your full name: ").strip().title()
    #while loop to allow the menu to keep being used until exited
    while True:
        option = display_menu(user_name)
        
        if option == "1":
            display_roster(names, ranks, divs, ids)

        elif option == "2":
            add_member(names, ranks, divs, ids, valid_ranks, valid_divs)

        elif option == "3":
            remove_member(names, ranks, divs, ids)
        
        elif option == "4":
            update_rank(names, ranks, ids, valid_ranks)
        
        elif option == "5":
            search_crew(names, ranks, divs, ids)


        elif option == "6":
            filter_by_division(names, ranks, divs, ids, valid_divs)
            
            
        elif option == "7":
            total_pay = calculate_payroll(ranks)
            print("\nTotal payroll cost:", total_pay, "credits")

       #elif option = "8":


        elif option == "9":
            print("Exiting Fleet Manager. Goodbye. ")
            break
        #all of the bulk of the code that calls each function and brings it together into the list
        #with the final elif number 9 being the exit function which allows the program to exit
main()
