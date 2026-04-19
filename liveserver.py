from livereload import Server


# Starts a local server that watches the HTML file for updates and automatically refreshes page
def start_server():
    server = Server()
    server.watch("./map/index.html")
    server.serve(root="./map/")


def main():
    start_server()


if __name__ == "__main__":
    main()
