from time import sleep

import folium

# Imports other project files and dependencies
import api_iss_position
import api_people_in_space


# Calls get_astronauts() and uses data to print nicely
def display_people_in_space():
    data = api_people_in_space.get_astronauts()
    if data is None:
        print("Kunne ikke hente data fra mennesker i verdensrommet.")
        return
    astronaut_count = data["number"]
    astronaut_people = data["people"]

    # Loops through list of astronauts and prints them as an ordered list
    # This should probably be done with enumerate
    print(f"Det er {astronaut_count} mennesker i verdensrommet akkurat nå.")
    for i, astronaut in enumerate(astronaut_people, start=1):
        print(f"{i}. {astronaut['name']} - {astronaut['craft']}")


# Calls get_iss_position() and uses data to print nicely
def display_iss_location():
    # This loop is messy and should be redone
    while True:
        data = api_iss_position.get_iss_position()
        if data is not None:
            lat = data["latitude"]
            lon = data["longitude"]

            # Generates a map with values from the API response.
            m = folium.Map([lat, lon], zoom_start=6, tiles="cartodb positron")

            # Places a marker with some flavour text
            folium.Marker(
                location=[lat, lon],
                tooltip="Wave to the ISS!",
                popup="The ISS waves back!",
                icon=folium.Icon(color="lightblue", icon="cloud"),
            ).add_to(m)

            # Saves map info in the map folder as index.html
            m.save("map/index.html")

            # These prints act as feedback for every API refresh
            print(f"The ISS is now at lat: {lat} lon: {lon}.")
            print("Map saved in index.html")

        # This makes sure the loop runs an iteration every 5 second
        # As reccommended by the API server
        sleep(5)


def main():
    display_people_in_space()
    display_iss_location()


if __name__ == "__main__":
    main()
