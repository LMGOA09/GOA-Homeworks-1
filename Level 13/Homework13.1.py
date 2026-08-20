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
car_profile["screen_type"] = "Anti-glare Matte Screen"
print(car_profile)

#7)
for key, value in car_profile.items():
    print(f"{key}: {value}")