import xml.etree.ElementTree as Et

# Parse the XML data
root = Et.parse("data/test_data_type_duplicate.xml")

# Create a dictionary to store the type names as keys
type_names = {}

# Iterate through the types
for type_elem in root.findall('type'):
    # Get the type name
    type_name = type_elem.get('name')

    # Check if the type name is already in the dictionary
    if type_name in type_names:
        # Print an error message
        print(f"Duplicate class: {type_name}")
    else:
        # Add the type name to the dictionary
        type_names[type_name] = True

    # Get the min and nominal values
    min_value = int(type_elem.find('min').text)
    nominal_value = int(type_elem.find('nominal').text)

    # Check if min is greater than nominal
    if min_value > nominal_value:
        # Print an error message
        print(f"Min > nominal for class {type_name}")
