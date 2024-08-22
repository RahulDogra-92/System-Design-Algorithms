# Description:
# Geohashing is a method of encoding latitude and longitude coordinates into a short string of letters and digits. S2 Geometry is a similar concept that divides the Earth's surface into cells.

# Use Case: Location-based services
# Python Example (Using Geohash):

import geohash2

# Encode a location into a geohash
latitude, longitude = 37.7749, -122.4194
geo = geohash2.encode(latitude, longitude, precision=7)

# Decode the geohash back into coordinates
lat, lon = geohash2.decode(geo)

print(f"Geohash: {geo}")
print(f"Decoded Coordinates: Latitude {lat}, Longitude {lon}")
