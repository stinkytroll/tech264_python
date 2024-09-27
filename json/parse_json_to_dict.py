import json

with open('servers.json', 'r') as json_file:  # Use 'r' to read to file
    servers = json.load(json_file)
    print(type(servers))  # Print the type of servers, <class 'dict'>

    print(servers["server1"])  # Print the information under key server1 and server2
    print(servers["server2"])

    for server_keys, server_values in servers.items():  # Loop through all keys and values of servers dict
        print(f"Key and value: '{server_keys}' = '{server_values}'")  # Print the keys and values of servers
        for sub_keys, sub_values in server_values.items():  # Loop through the keys and values inside each server
            print(f"Record key and sub value: '{sub_keys}' = '{sub_values}'")  # Print the sub keys and values
