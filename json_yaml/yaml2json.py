import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):  # Check to see if the script was run with at least one argument (YAML file)
        source_file = open(sys.argv[1], "r")  # Open in read mode
        source_content = yaml.safe_load(source_file)  # Safely loads the file
        source_file.close() # Close after reading
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)  # Exit if the file doesn't exist
# No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yamal2json.py <source_file.yaml> <target_file.json_yaml>")
    exit(1)

# 1. Convert the YAML to JSON - use json_yaml library
convert_json = json.dumps(source_content, indent=4)  # Converts the python dict into a JSON string with 4 indents

# 2. Save the YAML into a new file with the name for it received as an argument
# 2.1 Check the target file name was specified as an argument
if len(sys.argv) > 2:  # Check whether a second argument was provided
    target_file = sys.argv[2]

    # 2.2 Check the target file doesn't already exist
    if os.path.exists(target_file):
        print(f"ERROR: Target file '{target_file}' already exists.")
        exit(1)

    # 2.3 If previous conditions not met, then save JSON file
    with open(target_file, 'w') as yaml_file: # Writes the JSON file after if checks
        yaml_file.write(convert_json)
        print(f"JSON content successfully written to '{target_file}'")
else:
    # If no target file is provided, print the JSON content to the screen
    print("No target file specified. Outputting JSON to the screen:")
    print(convert_json)
