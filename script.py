import json
import emoji

modified_data = []
prénom_encountered = False  
def remove_emoji(string):
    return emoji.replace_emoji(string, replace='')

def process_prénom(value):
    if value and value.strip():  # Checking if the input is not empty or just whitespace
        return ','.join(char for char in value if char != ' ')
    return ''  # Returning an empty string if the input is empty or just whitespace


def process_value(key, value, prénom_encountered):
    if key == "Prénom":
        if prénom_encountered:
            return ',' + process_prénom(value)
        else:
            return process_prénom(value)
    else:
        return value

data =  {}
with open('data.json') as f:
#         # Load JSON data
        data = json.load(f)
             # Break the loop if no data is received
for d in data:
    # List of static field keys to remove
    static_fields_to_remove = [key for key in d.keys() if key.startswith("static_field")]
                
                # Removing static fields from dictionary
    for key in static_fields_to_remove:
        del d[key]
    products = d['products']
    result = []
    for product in products:
                    processed_values = []
                    for key, value in product.items():
                        if value is not None and value != '':
                            value_without_emojis = remove_emoji(value)
                            processed_value = process_value(key, value_without_emojis, prénom_encountered)
                            if key == "Prénom":
                                prénom_encountered = True
                            processed_values.append(processed_value)
                    result.append(','.join(processed_values))

    del d['products']
    final_result = ''.join(result)
    d["products"] = final_result
    modified_data.append(d)

            # Convert the modified data back to JSON
modified_json = json.dumps(modified_data, indent=2)

print(modified_json)


# Remove static fields from each dictionary in the tuple




