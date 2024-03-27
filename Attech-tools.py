import folium
import ipinfo

# Function to get location information from an IP address
def get_ip_location(ip_address):
    """
    Retrieves the location information for a given IP address using the IPInfo API.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing the location information, including latitude, longitude, city, region, and country.
    """
    handler = ipinfo.getHandler()
    details = handler.getDetails(ip_address)
    return {
        "latitude": details.latitude,
        "longitude": details.longitude,
        "city": details.city,
        "region": details.region,
        "country": details.country
    }

# Example usage
ip_address = input("Enter an IP address: ")
location_info = get_ip_location(ip_address)

# Create a map centered on the IP location
map = folium.Map(location=[location_info["latitude"], location_info["longitude"]], zoom_start=10)

# Add a marker to the map
folium.Marker(
    [location_info["latitude"], location_info["longitude"]],
    popup=f"{location_info['city']}, {location_info['region']}, {location_info['country']}"
).add_to(map)

# Display the map
map.save("ip_location.html")
print("Map saved as ip_location.html. Open the file in a web browser to view the location.")
