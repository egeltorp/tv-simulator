class TV:
    def __init__(self, tv_name, current_volume, current_channel, max_volume, max_channel):
        self.tv_name = tv_name
        self.current_volume = current_volume
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.max_channel = max_channel

    def change_channel(self, new_channel):
        if 1 <= new_channel <= self.max_channel:
            self.current_channel = new_channel
            return True
        else:
            return False

    def increase_volume(self):
        if self.current_volume != self.max_volume:
            current_volume += 1
            return True
        else:
            return False

    def decrease_volume(self)
        if 0 < self.current_volume < self.max_volume
            self.current_volume += 1
            return True
        else:
            return False
        
    def __str__(self):
        pass

    def str_for_file(self):
        pass