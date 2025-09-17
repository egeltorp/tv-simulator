class TV:
    def __init__(self, tv_name: str, max_channel: int, current_channel: int, max_volume: int, current_volume: int):
        self.tv_name = tv_name
        self.max_channel = max_channel
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.current_volume = current_volume

    def change_channel(self, new_channel):
        if 1 <= new_channel <= self.max_channel:
            self.current_channel = new_channel
            return True
        else:
            return False

    def increase_volume(self):
        if self.current_volume != self.max_volume:
            self.current_volume += 1
            return True
        else:
            return False

    def decrease_volume(self):
        if 1 <= self.current_volume:
            self.current_volume -= 1
            return True
        else:
            return False
        
    def __str__(self):
        return f"> {self.tv_name} | Kanal: {self.current_channel} | Volym: {self.current_volume}"

    def str_for_file(self):
        string = f"{self.tv_name},{self.max_channel},{self.current_channel},{self.max_volume},{self.current_volume}\n"
        return string

def tests():
        tv = TV("Vardagsrum TV", 100, 22, 10, 9)
        tv2 = TV("Sovrums TV", 50, 7, 20, 4)
        print(tv)
        print(tv2)
        print(tv.increase_volume())
        print(tv)
        print(tv2)
        print(tv.increase_volume())
        print(tv)
        print(tv2)
        print(tv.change_channel(55))
        print(tv)
        print(tv2)
        print(tv2.change_channel(55))
        print(tv)
        print(tv2)
        list = TV.str_for_file(tv)
        list = list.split(',')
        print(list)

if __name__ == "__main__":
    tests()
    
    
