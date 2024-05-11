def gps_coordinate(city):
    """
    Get GPS coordinates for a given city.
    
    Args:
    city (str): The name of the city.
    
    Returns:
    dict: Dictionary containing latitude and longitude.
    """
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json"}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if data:
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            return {"latitude": latitude, "longitude": longitude}
        else:
            print(f"No data found for city: {city}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Nominatim API: {e}")
        return None

# Test the function
if __name__ == "__main__":
    city = "Cairns"
    print(gps_coordinate(city))
