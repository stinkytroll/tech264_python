import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):  # Check to see if the script was run with at least one argument (YAML file)
        source_file = open(sys.argv[1], "r")  # Open in read mode
        source_content = json.load(source_file)  # Safely loads the file
        source_file.close()  # Close after reading
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)  # Exit if the file doesn't exist
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json_yaml> <target_file.yaml>")
    exit(1)

# 1. Convert the JSON to YAML - use yaml library
convert_yaml = yaml.dump(source_content)  # Converts to YAML string

# 2. Save the YAML into a new file with the name for it received as an argument
# 2.1 Check the target file name was specified as an argument
if len(sys.argv) > 2:  # Check if a second argument (target file) is provided
    target_file = sys.argv[2]  # Store the target file name

    # 2.2 Check the target file doesn't already exist
    if os.path.exists(target_file):
        print(f"ERROR: Target file '{target_file}' already exists.")
        exit(1)

    # 2.3 If previous conditions not met, then save YAML file
    with open(target_file, 'w') as yaml_file:  # Open target file in write mode
        yaml_file.write(convert_yaml)  # Write the YAML comment to the file
        print(f"YAML content successfully written to '{target_file}'")
else:
    # If no target file is provided, print the YAML content to the screen
    print("No target file specified. Outputting YAML to the screen:")
    print(convert_yaml)
