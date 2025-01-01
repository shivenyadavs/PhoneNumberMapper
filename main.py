import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Import the phone number (ensure 'myphone.py' contains a variable 'number')
from myphone import number

# Parse the phone number
parsed_number = phonenumbers.parse(number)

# Get the location description
location = geocoder.description_for_number(parsed_number, "en")
if not location:
    print("Unable to determine the location for the given phone number.")
    exit()

print(f"Location: {location}")

# Get the carrier service provider
service_provider = carrier.name_for_number(parsed_number, "en")
if not service_provider:
    print("Unable to determine the carrier for the given phone number.")
    exit()

print(f"Service Provider: {service_provider}")

# Set up OpenCage Geocode API
key = 'b6a1fdbfa3b3458698571fdd13bbe9b1'
geocoder_client = OpenCageGeocode(key)

# Perform geocoding for the location
try:
    results = geocoder_client.geocode(location)
    if not results:
        print("No geocoding results found for the location.")
        exit()
except Exception as e:
    print(f"Error during geocoding: {e}")
    exit()

# Extract latitude and longitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(f"Latitude: {lat}")
print(f"Longitude: {lng}")

# Create a folium map
try:
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    # Save the map to an HTML file
    my_map.save("mylocation.html")
    print("Map saved as 'mylocation.html'")
except Exception as e:
    print(f"Error creating or saving the map: {e}")
