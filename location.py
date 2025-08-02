import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+919048278833")
print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number, 'en'))
