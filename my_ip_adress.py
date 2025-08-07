import requests

response = requests.get('https://api.ipify.org?format=json')
ip_data = response.json()
print(f"Your public IP address is: {ip_data['ip']}")
