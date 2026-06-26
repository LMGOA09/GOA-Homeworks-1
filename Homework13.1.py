#4)
car_profile = {
    "company": "Alfa Romeo",
    "model": "GT Coupe",
    "year": 2005,
    "color": "Silver",
    "interface": "Sport-focused Gauges and Controls"
}

#5)
for value in car_profile.values():
    print(value)

#6)
# Adding a new key-value pair to the existing dictionary
car_profile["screen_type"] = "Anti-glare Matte Screen"

#7)
# Printing the key-value pairs in a clean, readable format
for key, value in car_profile.items():
    print(f"{key}: {value}")