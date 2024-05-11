def display_menu():
    """
    Display the menu options.
    """
    print("Help")
    print("====")
    print("The following commands are recognized.")
    print("Display help: wildlife> help")
    print("Exit the application: wildlife> exit")
    print("Display animal species in a city: wildlife> species [city]")
    print("Display animal sightings in a city: wildlife> sightings [city] [species]")
    print("Display venomous animal sightings in a city: wildlife> venomous [city]")

def main():
    """
    Main function to handle user input.
    """
    display_menu()
    while True:
        user_input = input("wildlife> ").strip().lower().split()
        command = user_input[0]
        if command == "help":
            display_menu()
        elif command == "exit":
            print("Exiting the program...")
            break
        elif command == "species":
            if len(user_input) == 2:
                city = user_input[1]
                search_species(city)
            else:
                print("Invalid command. Usage: wildlife> species [city]")
        elif command == "sightings":
            if len(user_input) == 3:
                city = user_input[1]
                species = user_input[2]
                search_sightings(species, city)
            else:
                print("Invalid command. Usage: wildlife> sightings [city] [species]")
        elif command == "venomous":
            if len(user_input) == 2:
                city = user_input[1]
                list_venomous_species(city)
            else:
                print("Invalid command. Usage: wildlife> venomous [city]")
        else:
            print("Invalid command. Type 'help' for available commands.")

def search_species(city):
    """
    Search and display animal species in a city.
    """
    # Stub function for now
    species_list = [
        {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]
    display_species(species_list)

def display_species(species_list):
    """
    Display the list of species.
    """
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        print(name)

def search_sightings(species, city):
    """
    Search and display animal sightings for a species in a city.
    """
    # Stub function for now
    sightings = [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]
    display_sightings(sightings)

def display_sightings(sightings):
    """
    Display the list of sightings.
    """
    for sighting in sightings:
        date = sighting["properties"]["StartDate"]
        location = sighting["properties"]["LocalityDetails"]
        print(f"Date: {date}, Location: {location}")

def list_venomous_species(city):
    """
    List and display venomous animal species in a city.
    """
    # Stub function for now
    venomous_species = [
        {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]
    display_species(venomous_species)

if __name__ == "__main__":
    main()

