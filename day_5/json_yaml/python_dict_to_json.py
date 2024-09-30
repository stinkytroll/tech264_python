import json
from pprint import pprint  # Import pretty print

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

json_formatting = json.dumps(servers_dict)  # Serialises a Python object into a JSON-formatted string.
pprint(json_formatting)

with open('servers.json', 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)
    print("Data saved to servers.json_yaml")

# with statement creates context for the execution of code. open() is then used to open a selected file for
# interaction. We use 'w' to enable write mode, allowing us to open the file for writing. We then convert and write
# the dictionary to JSON format as a json_yaml file, as well as a parameter for
# indenting the lines 4 times for readability.

