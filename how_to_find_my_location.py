# test.py# This script uses the geocoder library to get the current location based on IP address.
import geocoder


g = geocoder.ip('me')

if g.city and g.state and g.country:
    print(f"Your current location: {g.city}, {g.state}, {g.country}")
else:
    print("Could not determine your location.")
