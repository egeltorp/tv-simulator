def adjust_TV_menu(tv: TV):
    print("1. Byt kanal\n")
    print("2. Sänk volym")
    print("3. Höj volym")
    print("4. Huvudmenyn")
    
    options = list(range(1,5))
    while True:
        choice = int(input("[!] Välj 1-4"))
        if choice in options: break
        print("Ogiltigt. Försök igen!")
    
    if choice == 1:
        new_channel = int(input("Välj ny kanal: "))
        tv.change_channel(new_channel)
    elif choice == 2:
        tv.decrease_volume()
    elif choice == 3:
        tv.increase_volume()
    elif choice == 4:
        return False
    
if __name__ == "__main__":
    adjust_TV_menu()