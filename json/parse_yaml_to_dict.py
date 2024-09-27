import yaml

with open('converted.yaml', 'r') as yaml_file:  # Use 'r' to read to file
    details = yaml.safe_load(yaml_file)

    print(type(details))  # Print the type of servers, <class 'dict'>
    print(details)

