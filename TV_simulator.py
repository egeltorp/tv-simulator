from TV import TV

# read .txt file and convert strings to list of TV-class objs
def read_file(file_path):
    tv_list = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            tv_name, *variables  = line.split(',')
            variables = [int(v) for v in variables] # Convert all variables to int
            tv = TV(tv_name, *variables)
            tv_list.append(tv)
    return tv_list

# write all current TV-class objs to .txt with new/current values
def write_file(tv_list, file_path):
    with open(file_path, 'w') as file:
        for tv in tv_list:
            s = tv.str_for_file()
            file.write(s)

# menu to choose TV-class methods, returns choice: int
def adjust_TV_menu(tv: TV):
    quit_menu = False
    while True:
        if quit_menu:
            break

        print(f"\n{tv}")
        print("1. Byt kanal")
        print("2. Sänk volym")
        print("3. Höj volym")
        print("4. Huvudmenyn")
        
        # menu choice loop
        options = (1,2,3,4)
        while True:
            choice = int(input("\n[!] Välj 1-4: "))
            if choice in options:
                return choice
            print("Ogiltigt. Försök igen!")

# menu to choose which TV-class obj to currently simulate, returns obj
def select_TV_menu(tv_list: list):
    print("\n--- HUVUDMENYN ---")
    for i, tv in enumerate (tv_list, start=1):
        print(f"{i}. {tv}")
    print(f"{len(tv_list) + 1}. Avsluta")

    # tv select loop
    options = tuple(range(1, len(tv_list) + 1))
    while True:
        try:
            choice = int(input(f"\n[!] Välj 1-{len(tv_list) + 1}: "))
            if choice in options: 
                break
            elif choice == len(tv_list) + 1:
                return None
            print("Ogiltig TV. Försök igen!")
        except ValueError:
            print("Måste vara en siffra.")

    tv = tv_list[choice - 1]
    return tv

# full program loop
def simulator():
    # initializing and accessing list of TV-class objs
    tv_list = read_file("TV.txt")
    tv = tv_list[1]

    # intro text
    print("\n*** Välkommen till TV-simulatorn ***")
    print()

    # simulation loop
    while True:
        tv = select_TV_menu(tv_list)
        if tv == None:
            break
        while True:
            choice = adjust_TV_menu(tv)
            # choice 1: change channel
            if choice == 1:
                while True:
                    new_channel = int(input("Välj ny kanal: "))
                    if not tv.change_channel(new_channel):
                        print("Kanal finns inte.")
                    else:
                        tv.change_channel(new_channel)
                        break
            # choice 2: decrease vol, choice 3: increase vol
            elif choice in (2, 3):
                print(f"Volym: {tv.current_volume}")
                actions = {2: tv.decrease_volume, 3: tv.increase_volume}
                actions[choice]()
            # choice 4: exit TV adjust menu
            elif choice == 4:
                break
    
    # if both loops exited: quit program 
    # after saving current TV-class obj states
    write_file(tv_list, "TV.txt")
    print("Avslutar.")

# run simulator() if program is run in terminal as itself 
# and NOT imported as a module in other program
if __name__ == "__main__":
    simulator()
