from fastapi import FastAPI, HTTPException
from typing import List, Dict
import json
import emoji

app = FastAPI()

def remove_emoji(string):
    return emoji.replace_emoji(string, replace='')

def process_prénom(value):
    if value and value.strip():  
        return ','.join(char for char in value if char != ' ')
    return ''

def process_value(key, value, prénom_encountered):
    if key == "Prénom":
        if prénom_encountered:
            return ',' + process_prénom(value)
        else:
            return process_prénom(value)
    else:
        return value

@app.post("/process_data")
async def process_data(data: List[Dict]):
    modified_data = []
    for d in data:
        static_fields_to_remove = [key for key in d.keys() if key.startswith("static_field")]
        for key in static_fields_to_remove:
            del d[key]
        prénom_encountered = False
        products = d.get('products', [])
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
    return modified_data

# Example usage:
# If you have a JSON payload to send to this endpoint, you can use a tool like Postman or cURL to send a POST request to http://127.0.0.1:8000/process_data with your JSON data in the body.
# The response will contain the modified JSON data.

# For development purposes, you can run the FastAPI server like this:
# uvicorn main:app --reload
