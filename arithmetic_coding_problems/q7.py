def calculate_wci(t, v):
    return 13.12 + (0.6215 * t) - (11.37 * v**0.16) + (0.3965 * t * v**0.16)


air_temp = float(input("Enter air temperature in Celcius: "))
wind_speed = float(input("Enter wind speed in km/h: "))

wci = calculate_wci(air_temp, wind_speed)

print(f"Wind Chill Index: {round(wci, 2)}")
