from TV import TV

def read_file(file_path):
    tv_list = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            tv_name, *variables  = line.split(',')
            for v in variables:
                v = int(v)
            print(variables)
    return tv_list

tv_list = read_file("TV.txt")

