def get_species_list(coordinate, radius):
    """
    Get a list of species in an area defined by GPS coordinates and radius.
    
    Args:
    coordinate (dict): Dictionary containing latitude and longitude.
    radius (int): Radius in meters.
    
    Returns:
    list: List of species in the specified area.
    """
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

# Test the function
if __name__ == "__main__":
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000
    print(get_species_list(coordinate, radius))

