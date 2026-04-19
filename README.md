# Space API

Small Python project that fetches live space data from Open Notify.

It prints the people currently in space, then keeps updating a Folium map with the current ISS position.

## Requirements

- Python 3.13 or newer
- Internet connection
- Python packages:
  - `requests`
  - `folium`
  - `livereload`

## Run

Run this project inside a Python virtual environment using Python 3.13 or newer.

Install the dependencies inside your virtual environment:

```bash
python -m pip install .
```

Start the live server and the main program in separate terminal instances:

```bash
python liveserver.py
```

```bash
python main.py
```

Open the live server page in your browser. The browser must be connected to the live server, or refreshed after the live server is running, so it notices the connection.

## Todo

- Add timeouts and retries for API requests.
- Use async so the map updates and live server can run together from main.py.
