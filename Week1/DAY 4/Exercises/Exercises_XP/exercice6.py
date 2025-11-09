
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names_list):
    for i in range(len(names_list)):
        names_list[i] = "The Great " + names_list[i]
        print(names_list[i])


show_magicians(magician_names)

make_great(magician_names)