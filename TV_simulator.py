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

tv_list = read_file("TV.txt")

tv_list[0].increase_volume()

write_file(tv_list, "TV.txt")

for tv in tv_list:
    print(tv)
