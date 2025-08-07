# Install with: pip install ipinfo
import ipinfo

# Get a free token from https://ipinfo.io/signup
access_token = 'ca157dd0a8f6b6'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

print(f"City: {details.city}")
print(f"Region: {details.region}")
print(f"Country: {details.country}")
