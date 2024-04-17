from urllib import request
from fastapi import FastAPI
import requests
from typing import List, Dict
import openpyxl
import emoji
import pprint
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
def compare_products(filename, products):
    # Open the Excel file
    wb = openpyxl.load_workbook(filename)
    
    # Select the first sheet
    sheet = wb.active
    
    # Initialize a list to store matched values
    matched_values = []
    
    # Iterate through each row
    for row in sheet.iter_rows(values_only=True):
        # Assuming the products are in the first column (column A)
        product = row[4]
        # If the product is found in the given products list
        if product in products:
            # Append the row data to the matched values list
            matched_values.append(row)
    
    # Close the workbook
    wb.close()
    
    return matched_values
@app.post("/process_data")
async def process_data(data: List[Dict]):
    modified_data = []
    for d in data:
        
        d["StoreKey"] = "KITIMIMITEST"
        d["OrderType"] = "Sell" 
        full_name = d["shipping_full_name"]  
        first_name, last_name = full_name.split(maxsplit=1) 
        d["Delivery"] = {
    "Recipient":{
                  "RecipLanguageCode":"FR",
                  "RecipCompanyName":"",
                  "RecipFirstName":first_name,
                  "RecipLastName":last_name,
                  "RecipAdr2":d["shipping_address_1"],
                  "RecipAdr1":d["shipping_address_2"],
                  "RecipAdr0":"",
                  "RecipZipCode":d["shipping_postcode"],
                  "RecipCity":d["shipping_city"],
                  "RecipCountryCode":d["shipping_country"],
                  "RecipCountryLib":"Réunion",
                  "Recipemail":d["billing_email"],
                  "RecipMobileNumber":"",
                  "RecipPhoneNumber":d["shipping_phone"],
                  "DeliveryRelayCountry":"",
                  "DeliveryRelayNumber":""
               },
               "Parcel":{
                  "ShippingServiceKey":"COLMEGA",
                  "ShippingProductCode":"CDS",
                  "InsurranceYN":"N",
                  "InsurranceCurrency":"EUR",
                  "ParcelValueCurrency":"EUR",
                  "ParcelWeight":"97.5",
                  "WeightUnit":"g"
               },
               "Sender":{
                  "SenderLanguageCode":"FR",
                  "SenderAdr2":"51 Rue de Toufflers",
                  "SenderAdr3":"POUR KITIMIMI",
                  "Sendercity":" Lys-lez-Lannoy",
                  "SenderzipCode":"59390",
                  "SendercompanyName":" Stock logistic",
                  "SendercountryCode":"FR",
                  "SendercountryLib":"FRANCE",
                  "SenderphoneNumber":"0033320200909",
                  "Senderemail":"hello@kitimimi.com"
               }

}       
        static_fields_to_remove = [key for key in d.keys() if key.startswith("static_field")]
        for key in list(d.keys()):
            if key.startswith("customer_note"):
                new_key = "CheckoutMessage" + key[len("customer_note"):]
                d[new_key] = d.pop(key)
        for key in list(d.keys()):
            if key.startswith("order_number"):
                new_key = "OrderKey" + key[len("order_number"):]
                d[new_key] = d.pop(key)
        for key in list(d.keys()):
            if key.startswith("order_date"):
                new_key = "OrderDate" + key[len("order_date"):]
                d[new_key] = d.pop(key)
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
                    if r"\u00é" in processed_value:
                        processed_value = processed_value.replace(r'\u00é', 'e')
                    if r"é" in processed_value:
                        processed_value = processed_value.replace(r'é', 'e')
                    if key == "Prénom":
                        prénom_encountered = True
                    
                    #print("product is",processed_value)
                    processed_values.append(processed_value)
            result.append(','.join(processed_values))
        del d['products']
        final_result = ''.join(result)
        
        checking=compare_products("./list.xlsx",final_result)
        formatted_data = {}
        for item in checking:
            sku = item[2]  # SKU is the fourth element
            quantity = 0  # Quantity is the sixth element
            weight =  item[6]   # Weight is the seventh element, if None, make it empty
            ProductName=item[4]
            if sku not in formatted_data:
                # If SKU not already in formatted data, initialize its entry
                formatted_data[sku] = {
                    "SKU": sku,
                    "Quantity": quantity,
                    "ProductName": ProductName,  # Empty for now, will be filled later
                    "CN23Category": "",
                    "PriceExclTax": "",
                    "Weight": weight,
                    "EANCode": "",
                    "VariationID": "",
                    "VAT": ""
                }
            else:
                # If SKU already exists, add the quantity
                formatted_data[sku]["Quantity"] += quantity

        # Convert the dictionary to a list of formatted dictionaries
        formatted_list = list(formatted_data.values())
        d["products"] = formatted_list
        if 'billing_email' in d:
            del d['billing_email']
        if 'order_number' in d:
            del d['order_number']
        if 'shipping_address_1' in d:
            del d['shipping_address_1']
        if 'shipping_address_2' in d:
            del d['shipping_address_2']
        if 'shipping_city' in d:
            del d['shipping_city']
        if 'shipping_country' in d:
            del d['shipping_country']
        if 'shipping_full_name' in d:
            del d['shipping_full_name']
        if 'shipping_phone' in d:
            del d['shipping_phone']
        if 'shipping_postcode' in d:
            del d['shipping_postcode']
        modified_data.append(d)

    # Construct response data
    response_data ={
        "Request": 
    {
        "Orders": modified_data
    }}
    
    # Construct response headers
    headers = {
        "Token": "KEy5YrFM3EieHYc+CSoFTZlFBtVonvat" 
    }

    api_url = "https://sl.atomicseller.com/Api/Order/CreateOrders"
    
    print(response_data)
    response = requests.post(
        url=api_url,
        json=response_data,
        headers=headers
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Response sent successfully.")
    else:
        print("Failed to send response. Status code:", response.status_code)