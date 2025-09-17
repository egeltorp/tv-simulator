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

def adjust_TV_menu():
    print("1. Byt kanal")
    print("2. Höj volym")
    print("3. Sänk volym")
    print("4. Återgå till huvudmenyn")

    while True:
        choice = int(input("[!] Välj 1-4: "))
        if choice not in [1,2,3,4]:
            print("Ogiltigt val, försök igen.")
        else:
            break
    return choice

def simulator():
    print("--- Välkommen till TV-simulatorn ---")
    adjust_TV_menu()

    pass

if __name__ == "__main__":
    simulator()
