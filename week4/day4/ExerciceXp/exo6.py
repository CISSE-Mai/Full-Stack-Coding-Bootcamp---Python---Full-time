magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names) :
    list(filter(lambda magiciens: print(magiciens),magician_names))
def make_great(liste) :
    for i in range(0,len(liste)):
        liste[i] += " the Great"
make_great(magician_names)
show_magicians(magician_names)