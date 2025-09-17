from TV import TV

def read_file(file_path):
    tv_list = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            tv_name, *variables  = line.split(',')
            variables = [int(v) for v in variables] # Convert all variables to int
            tv = TV(tv_name, *variables)
            tv_list.append(tv)
    return tv_list

def write_file(tv_list, file_path):
    with open(file_path, 'w') as file:
        for tv in tv_list:
            s = tv.str_for_file()
            file.write(s)

def adjust_TV_menu(tv: TV):
    while True:
        print(f"\n{tv}")
        print("1. Byt kanal")
        print("2. Sänk volym")
        print("3. Höj volym")
        print("4. Huvudmenyn")
        
        # menu choice loop
        options = (1,2,3,4)
        while True:
            choice = int(input("\n[!] Välj 1-4: "))
            if choice in options: break
            print("Ogiltigt. Försök igen!")
        
        if choice == 1:
            while True:
                new_channel = int(input("Välj ny kanal: "))
                if not tv.change_channel(new_channel):
                    print("Kanal finns inte.")
                else:
                    tv.change_channel(new_channel)
                    break
        elif choice in (2, 3):
            print(f"Volym: {tv.current_volume}")
            actions = {2: tv.decrease_volume(), 3: tv.increase_volume()}
            actions[choice]()
        elif choice == 4:
            break
        break

def simulator():
    # initializing
    tv_list = read_file("TV.txt")
    tv = tv_list[1]
    print("--- Välkommen till TV-simulatorn ---")

    adjust_TV_menu(tv)

    pass

if __name__ == "__main__":
    simulator()
