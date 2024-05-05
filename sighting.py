 display_menu();   
def display_menu():
    print("Help")
    print("===")
    print("The following commands are recognised.")
    #Formatiing the menu to show align
    print('Display help {:>20}  wildlife> help'.format(''))
    print('Display animal species in a city   wildlife> species Cairns')
    print('Display venonmous species wildlife> species Cairns venomous')
    print('Display animal sightings in a city wildlife> sightings Cairns 1039')
    print('Exit the application {:>12}  wildlife> exit\n'.format(''))


def main():
    display_menu()
    while(True):
        comm = input().split(' ')
        print("\n")
        if(comm[0]=="exit"):
            exit(0)
        elif(comm[0]=="help"):
            display_menu()
        elif(comm[0]=="species"):
            
            if len(comm)>2:
                display_species(filter_venomous(search_species(comm[1])))
            else:
                display_species(search_species(comm[1]))
            
        elif(comm[0]=="sightings"):
            display_sightings(search_sightings(comm[2],comm[1]))
        else:
            print("ERROR: Unrecognized Command. Please check and try again.")
            display_menu()

def search_species(city):
