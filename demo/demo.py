import folium
import requests

# Oppgave 1

# Astronauts data
response_astronauts = requests.get("http://api.open-notify.org/astros.json")

# Kun bearbeid responsen hvis den er "ok"
if response_astronauts.status_code == 200:
    data_astronauts = response_astronauts.json()
else:
    print(response_astronauts.status_code)
    print("Wrong status code")

# Lagrer verdi av "number" i astronauts_count
astronauts_count = data_astronauts["number"]
# Lagrer liste med astronauter i astronaut_people
astonauts_people = data_astronauts["people"]

# Print hvor mange mennesker det er i verdensrommet
print(f"Det er {astronauts_count} mennesker i verdensrommet akkurat nå.")

# Print en nummerert liste med hver astronauts navn og fartøy
i = 1
for astronaut in astonauts_people:
    print(f"{i}. {astronaut['name']} - {astronaut['craft']}")
    i += 1

# Oppgave 2

# ISS data
response_iss = requests.get("http://api.open-notify.org/iss-now.json")

# Kun bearbeid responsen hvis den er "ok"
if response_iss.status_code == 200:
    data_iss = response_iss.json()
else:
    print(response_iss.status_code)
    print("Wrong status code")

# Save latitude and longitude in respective variables
lat = data_iss["iss_position"]["latitude"]
lon = data_iss["iss_position"]["longitude"]

# Folium section
#
# Create a folium map and save in variable m
kart = folium.Map((lat, lon), zoom_start=5, tiles="cartodb positron")

# Lag en markør på kartet
folium.Marker(
    # Bruk lengde- og breddegradene fra API responsen
    location=[lat, lon],
    tooltip="Dette er hvor ISS er!",
    icon=folium.Icon(icon="cloud"),
).add_to(kart)

# Lagre folium kartet "m" i
kart.save("iss.html")
