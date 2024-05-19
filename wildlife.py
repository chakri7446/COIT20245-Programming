import requests

def get_species_list(coordinate, radius):
    '''
    Get a list of species in an area defined by GPS coordinates and radius.
    
    Args:
    coordinate (dict): Dictionary containing latitude and longitude.
    radius (int): Radius in meters.
    
    Returns:
    list: List of species in the specified area.
    '''
    base_url = "https://apps.des.qld.gov.au/species/?op=getspecieslist"
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    params = {
        "kingdom": "animals",
        "circle": f"{lat},{lon},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "SpeciesSightingSummariesContainer" in data:
        return data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    else:
        return None

def get_surveys_by_species(coordinate, radius, taxonid):
    '''
    Retrieve a list of animal surveys in an area for a given species (taxonid).
    
    Args:
    coordinate (dict): Dictionary containing latitude and longitude.
    radius (int): Radius in meters.
    taxonid (int): The taxonomic identifier for the species.
    
    Returns:
    list: List of surveys for the specified species in the specified area.
    '''
    base_url = "https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies"
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    params = {
        "taxonid": str(taxonid),
        "circle": f"{lat},{lon},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data.get("features", [])

def search_sightings(taxonid, coordinate, radius):
    '''
    Search for incidental sightings of a species in a specified area and filter by "INCIDENTAL" site code.
    
    Args:
    taxonid (int): The taxonomic identifier for the species.
    coordinate (dict): Dictionary containing latitude and longitude.
    radius (int): Radius in meters.
    
    Returns:
    list: List of incidental sightings.
    '''
    surveys = get_surveys_by_species(coordinate, radius, taxonid)
    incidental_sightings = [s for s in surveys if s.get("properties", {}).get("SiteCode") == "INCIDENTAL"]
    return incidental_sightings

def earliest(sightings):
    '''
    Returns the sighting with the earliest start date.
    
    Args:
    sightings (list): List of sighting dictionaries.
    
    Returns:
    dict: The sighting with the earliest date.
    '''
    return min(sightings, key=lambda x: x.get("properties", {}).get("StartDate"), default=None)

def sort_by_date(sightings):
    '''
    Returns sightings sorted by date.
    
    Args:
    sightings (list): List of sighting dictionaries.
    
    Returns:
    list: Sightings sorted by date.
    '''
    return sorted(sightings, key=lambda x: x.get("properties", {}).get("StartDate"))

def display_sightings(sightings):
    '''
    Display and sort sightings by date.
    
    Args:
    sightings (list): List of sighting dictionaries.
    '''
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Date: {sighting.get('properties', {}).get('StartDate')}, Location: {sighting.get('properties', {}).get('LocalityDetails')}")

if __name__ == "__main__":
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000
    taxonid = 860
    
    # Try to get a list of species
    species_list = get_species_list(coordinate, radius)
    print("Species List:", species_list)
    
    # Try to get surveys by species
    surveys = get_surveys_by_species(coordinate, radius, taxonid)
    print("Surveys:", surveys)
    
    # Search for incidental sightings
    incidental_sightings = search_sightings(taxonid, coordinate, radius)
    print("Incidental Sightings:", incidental_sightings)
    
    # Display and sort these sightings if any
    if incidental_sightings:
        display_sightings(incidental_sightings)
    else:
        print("No incidental sightings found.")
