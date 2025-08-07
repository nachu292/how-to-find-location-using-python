import geocoder

target_ip = "8.8.8.8"  # Replace with the IP address you want to look up
g = geocoder.ip(target_ip)

if g.city and g.state and g.country:
    print(f"Location for {target_ip}: {g.city}, {g.state}, {g.country}")
else:
    print(f"Could not determine the location for {target_ip}.")
