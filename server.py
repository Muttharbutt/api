from fastapi import FastAPI
import requests
from typing import List, Dict
import openpyxl
import emoji
import json
from unidecode import unidecode
app = FastAPI()
prename=""
checklang=""
productslist=[
    {
        "Brand": "1",
        "Type": "01",
        "Number": "001",
        "SKU": "101001",
        "FR": "Planche de Couverture",
        "Weight (g)": "90",
 
        "EN": "Cover board",
        "DE": "Abdeckungstafel"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "001",
        "SKU": "102001",
        "FR": "Gestes du quotidien",
        "Weight (g)": "150",
 
        "EN": "Daily life 1",
        "DE": "Alltag"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "002",
        "SKU": "102002",
        "FR": "Gestes du quotidien 2",
        "Weight (g)": "150",
 
        "EN": "Daily life 2",
        "DE": "Alltag 2"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "003",
        "SKU": "102003",
        "FR": "Gestes du quotidien 3",
        "Weight (g)": "150",
 
        "EN": "Daily life 3",
        "DE": "Alltag 3"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "004",
        "SKU": "102004",
        "FR": "Formes - couleurs et tailles",
        "Weight (g)": "150",
 
        "EN": "Shapes - Colors & Sizes",
        "DE": "FORMEN - FARBEN& GROBEN"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "005",
        "SKU": "102005",
        "FR": "Denombrement",
        "Weight (g)": "150",
 
        "EN": "Count",
        "DE": "Aufzahlung"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "006",
        "SKU": "102006",
        "FR": "Cadre temporel - Jour et Nuit",
        "Weight (g)": "150",
 
        "EN": "Time Frame - Day & Night",
        "DE": "Zeitrahmen - Tag & Nacht"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "007",
        "SKU": "102007",
        "FR": "Logique et Puzzle",
        "Weight (g)": "150",
 
        "EN": "Logic & Puzzle",
        "DE": "Logik & Ratsel"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "008",
        "SKU": "102008",
        "FR": "Pizza et Horloge",
        "Weight (g)": "150",
 
        "EN": "Pizza & Clock",
        "DE": "Pizza & Uhr"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "009",
        "SKU": "102009",
        "FR": "Schema corporel fille",
        "Weight (g)": "150",
 
        "EN": "Girl Body Map",
        "DE": "Der Madchenkoper"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "010",
        "SKU": "102010",
        "FR": "Schema corporel garcon",
        "Weight (g)": "150",
 
        "EN": "Boy Body Map",
        "DE": "Der Jungenkorper"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "011",
        "SKU": "102011",
        "FR": "Fruits et Legumes",
        "Weight (g)": "150",
 
        "EN": "Fruits & VEGGIES",
        "DE": "Obst & Gemuse"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "012",
        "SKU": "102012",
        "FR": "Saisons",
        "Weight (g)": "150",
 
        "EN": "Seasons",
        "DE": "Jahreszeiten"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "013",
        "SKU": "102013",
        "FR": "Cadre spatial et Transport",
        "Weight (g)": "150",
 
        "EN": "Space Frame & Transport",
        "DE": "Trousse  Rose"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "014",
        "SKU": "102014",
        "FR": "Toucher et Memorisation",
        "Weight (g)": "150",
 
        "EN": "Touch & Memorization",
        "DE": "Beruhren & speichern"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "015",
        "SKU": "102015",
        "FR": "Animaux - Jungle et Ferme",
        "Weight (g)": "150",
 
        "EN": "Animals - Jungle & Farm",
        "DE": "Tiere - Dschungel & Bauernhof"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "016",
        "SKU": "102016",
        "FR": "Table",
        "Weight (g)": "150",
 
        "EN": "Table",
        "DE": "Am Tisch"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "017",
        "SKU": "102017",
        "FR": "Animaux - mer et Dexterite",
        "Weight (g)": "150",
 
        "EN": "Sea Animals & Dexterity",
        "DE": "Meereslebewesen & Geschicklichkeit"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "018",
        "SKU": "102018",
        "FR": "Animaux -Desert et Banquise",
        "Weight (g)": "150",
 
        "EN": "Animals - Desert & Ice",
        "DE": "Tiere - Wuste & Eis"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "019",
        "SKU": "102019",
        "FR": "Emotions",
        "Weight (g)": "150",
 
        "EN": "Emotions",
        "DE": "Emotionen"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "020",
        "SKU": "102020",
        "FR": "Cycle - Eau et Fleur",
        "Weight (g)": "150",
 
        "EN": "Cycle - Water & Flower",
        "DE": "Zyklus - Wasser & Blume"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "021",
        "SKU": "102021",
        "FR": "Dessin et Ecriture",
        "Weight (g)": "150",
 
        "EN": "Drawing & Writing",
        "DE": "Zeichnen & Schreiben"
    },
    {
        "Brand": "1",
        "Type": "02",
        "Number": "022",
        "SKU": "102022",
        "FR": "Vetements",
        "Weight (g)": "150",
 
        "EN": "Clothes",
        "DE": "Kleidung"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "001",
        "SKU": "103001",
        "FR": "Lacets rouges",
        "Weight (g)": "10",
 
        "EN": "Red Laces",
        "DE": "Rot"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "002",
        "SKU": "103002",
        "FR": "Lacets verts",
        "Weight (g)": "10",
 
        "EN": "Green Laces",
        "DE": "Grun"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "003",
        "SKU": "103003",
        "FR": "Lacets bleus",
        "Weight (g)": "10",
 
        "EN": "Blue Laces",
        "DE": "Blau"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "004",
        "SKU": "103004",
        "FR": "Lacets jaunes",
        "Weight (g)": "10",
 
        "EN": "Yellow Laces",
        "DE": "Gelb"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "005",
        "SKU": "103005",
        "FR": "Lacets oranges",
        "Weight (g)": "10",
 
        "EN": "Orange Laces",
        "DE": "Orangefarben"
    },
    {
        "Brand": "1",
        "Type": "03",
        "Number": "006",
        "SKU": "103006",
        "FR": "Lacets roses",
        "Weight (g)": "10",
 
        "EN": "Pink Laces",
        "DE": "Rosa"
    },
    {
        "Brand": "1",
        "Type": "04",
        "Number": "001",
        "SKU": "104001",
        "FR": "Coffret",
        "Weight (g)": "500",
 
        "EN": "Color box",
        "DE": "Farbkasten"
    },
    {
        "Brand": "1",
        "Type": "05",
        "Number": "001",
        "SKU": "105001",
        "FR": "Cube de rangement",
        "Weight (g)": "600",
 
        "EN": "Storage cube",
        "DE": "Kitibook Aufbewahrungsbox"
    },
    {
        "Brand": "1",
        "Type": "06",
        "Number": "001",
        "SKU": "106001",
        "FR": "Trousse Vert",
        "Weight (g)": "95",
 
        "EN": "Green purse",
        "DE": "Grune Handtasche"
    },
    {
        "Brand": "1",
        "Type": "06",
        "Number": "002",
        "SKU": "106002",
        "FR": "Trousse Bleue",
        "Weight (g)": "95",
 
        "EN": "Blue purse",
        "DE": "Blaue Handtasche"
    },
    {
        "Brand": "1",
        "Type": "06",
        "Number": "003",
        "SKU": "106003",
        "FR": "Trousse Orange",
        "Weight (g)": "95",
 
        "EN": "Orange purse",
        "DE": "Orange Handtasche"
    },
    {
        "Brand": "1",
        "Type": "06",
        "Number": "004",
        "SKU": "106004",
        "FR": "Trousse Rose",
        "Weight (g)": "95",
 
        "EN": "Pink purse",
        "DE": "Pink Handtasche"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "001",
        "SKU": "107001",
        "FR": "A",
        "Weight (g)": "4",
 
        "EN": "A",
        "DE": "A"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "002",
        "SKU": "107002",
        "FR": "B",
        "Weight (g)": "4",
 
        "EN": "B",
        "DE": "B"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "003",
        "SKU": "107003",
        "FR": "C",
        "Weight (g)": "4",
 
        "EN": "C",
        "DE": "C"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "004",
        "SKU": "107004",
        "FR": "D",
        "Weight (g)": "4",
 
        "EN": "D",
        "DE": "D"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "005",
        "SKU": "107005",
        "FR": "E",
        "Weight (g)": "4",
 
        "EN": "E",
        "DE": "E"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "006",
        "SKU": "107006",
        "FR": "F",
        "Weight (g)": "4",
 
        "EN": "F",
        "DE": "F"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "007",
        "SKU": "107007",
        "FR": "G",
        "Weight (g)": "4",
 
        "EN": "G",
        "DE": "G"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "008",
        "SKU": "107008",
        "FR": "H",
        "Weight (g)": "4",
 
        "EN": "H",
        "DE": "H"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "009",
        "SKU": "107009",
        "FR": "I",
        "Weight (g)": "4",
 
        "EN": "I",
        "DE": "I"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "010",
        "SKU": "107010",
        "FR": "J",
        "Weight (g)": "4",
 
        "EN": "J",
        "DE": "J"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "011",
        "SKU": "107011",
        "FR": "K",
        "Weight (g)": "4",
 
        "EN": "K",
        "DE": "K"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "012",
        "SKU": "107012",
        "FR": "L",
        "Weight (g)": "4",
 
        "EN": "L",
        "DE": "L"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "013",
        "SKU": "107013",
        "FR": "M",
        "Weight (g)": "4",
 
        "EN": "M",
        "DE": "M"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "014",
        "SKU": "107014",
        "FR": "N",
        "Weight (g)": "4",
 
        "EN": "N",
        "DE": "N"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "015",
        "SKU": "107015",
        "FR": "O",
        "Weight (g)": "4",
 
        "EN": "O",
        "DE": "O"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "016",
        "SKU": "107016",
        "FR": "P",
        "Weight (g)": "4",
 
        "EN": "P",
        "DE": "P"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "017",
        "SKU": "107017",
        "FR": "Q",
        "Weight (g)": "4",
 
        "EN": "Q",
        "DE": "Q"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "018",
        "SKU": "107018",
        "FR": "R",
        "Weight (g)": "4",
 
        "EN": "R",
        "DE": "R"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "019",
        "SKU": "107019",
        "FR": "S",
        "Weight (g)": "4",
 
        "EN": "S",
        "DE": "S"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "020",
        "SKU": "107020",
        "FR": "T",
        "Weight (g)": "4",
 
        "EN": "T",
        "DE": "T"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "021",
        "SKU": "107021",
        "FR": "U",
        "Weight (g)": "4",
 
        "EN": "U",
        "DE": "U"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "022",
        "SKU": "107022",
        "FR": "V",
        "Weight (g)": "4",
 
        "EN": "V",
        "DE": "V"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "023",
        "SKU": "107023",
        "FR": "W",
        "Weight (g)": "4",
 
        "EN": "W",
        "DE": "W"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "024",
        "SKU": "107024",
        "FR": "X",
        "Weight (g)": "4",
 
        "EN": "X",
        "DE": "X"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "025",
        "SKU": "107025",
        "FR": "Y",
        "Weight (g)": "4",
 
        "EN": "Y",
        "DE": "Y"
    },
    {
        "Brand": "1",
        "Type": "07",
        "Number": "026",
        "SKU": "107026",
        "FR": "Z",
        "Weight (g)": "4",
 
        "EN": "Z",
        "DE": "Z"
    },]
def remove_accents(text):
    return unidecode(text)
def remove_emoji(string):
    return emoji.replace_emoji(string, replace='')
def process_prénom(value):
    if value and value.strip():  
        return ','.join(char for char in value if char != ' ')
    return ''
def checklangauge(value):
    global checklang
    products=value.upper()
    products_list = products.split(',')
    first_product = products_list[0]
    if first_product=='TABLE':
        first_product = products_list[1]
    if first_product=='EMOTIONS':
        first_product = products_list[1]
    for row in productslist:
        product = row['FR']
        product_upper = product.upper()
        if product_upper==first_product:
            checklang='fr'
        product = row['EN']
        product_upper = product.upper()
        if product_upper==first_product:
            checklang='en'
        product = row['DE']
        product_upper = product.upper()
        if product_upper==first_product:
            checklang='de'
def process_value(key, value, prénom_encountered):
    global prename
    if key == "Prénom":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value)
    if key == "Child Name":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value) 
    if key == "Vorname":
        if prénom_encountered:
            prename=value
            return '' + process_prénom(value)
        else:
            return process_prénom(value)  
    else:
        return value
def compare_products(filename, products):
    # Convert products to uppercase
    products_list = products.split(',')
    products_upper = [product.upper() for product in products_list]
    products_upper = [product.replace("&AMP;", "&").replace("Ö", "O").replace("Ä", "A").replace("Ü", "U") for product in products_upper]
    products_upper=[s.strip() for s in products_upper]
    matched_values = []
    for row in productslist:
        if checklang=="fr":
            product = row['FR']
        if checklang=="de":
            product = row['DE']
        if checklang=="en":
            product = row['EN']
        product_upper = product.upper()
        for pro in products_upper:
            if pro==product_upper:
                matched_values.append(row)
    return matched_values
@app.post("/process_data")
async def process_data(data: List[Dict]):
    modified_data = []
    totalwieght=0
    for d in data:
        
        d["StoreKey"] = "KITIMIMI"
        d["OrderType"] = "Sell" 
        full_name = d["shipping_full_name"]  
        first_name, last_name = full_name.split(maxsplit=1) 
        
        static_fields_to_remove = [key for key in d.keys() if key.startswith("static_field")]
        # for key in list(d.keys()):
        #     if key.startswith("customer_note"):
        #         new_key = "CheckoutMessage" + key[len("customer_note"):]
        #         d[new_key] = d.pop(key)
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
        target_keys = ["Prénom", "Child Name", "Vorname"]
        formatted_data = {}
        for product in products:
            final_result=''
            processed_values = []
            for key, value in product.items():
                value = remove_accents(value)
                if key not in target_keys and value is not None and value != '':
                    checklangauge(value)
                    break
            for key, value in product.items():
                value = remove_accents(value)
                if value is not None and value != '':
                    value_without_emojis = remove_emoji(value)
                    if key == "Prénom":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)    
                    if key == "Child Name":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)
                    if key == "Vorname":
                        prénom_encountered = True
                        if "CheckoutMessage" not in d:
                            d["CheckoutMessage"] =remove_accents(value) 
                        else:
                            d["CheckoutMessage"] =d["CheckoutMessage"] +" ,"+ remove_accents(value)  
                    processed_value = process_value(key, value_without_emojis, prénom_encountered)
                    if r"\u00é" in processed_value:
                        processed_value = processed_value.replace(r'\u00é', 'e')
                    if r"é" in processed_value:
                        processed_value = processed_value.replace(r'é', 'e')
                    if r"ç" in processed_value:
                        processed_value = processed_value.replace(r'ç', 'c')
                    processed_values.append(processed_value)
            result.append(','.join(processed_values))
            final_result = ','.join(result)
            checking=compare_products("./list.xlsx",final_result)
            result=[]
            for item in checking:
                sku =item['SKU'] 
                quantity = 1  # Quantity is the sixth element
                weight = int( item['Weight (g)'] )   # Weight is the seventh element, if None, make it empty
                ProductName=item['FR']  
                totalwieght=weight+totalwieght
                if sku not in formatted_data:
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
                    formatted_data[sku]["Quantity"] += quantity
        # Convert the dictionary to a list of formatted dictionaries
        formatted_list = list(formatted_data.values())
        del d['products']
        d["products"] = formatted_list
        d["Delivery"] = {
        "Recipient":{
                    "RecipLanguageCode":"FR",
                    "RecipCompanyName":"",
                    "RecipFirstName":remove_accents(first_name),
                    "RecipLastName":remove_accents(last_name),
                    "RecipAdr2":"",
                    "RecipAdr1":remove_accents(d["shipping_address_2"]),
                    "RecipAdr0":remove_accents(d["shipping_address_1"]),
                    "RecipZipCode":remove_accents(d["shipping_postcode"]),
                    "RecipCity":remove_accents(d["shipping_city"]),
                    "RecipCountryCode":remove_accents(d["shipping_country"]),
                    "RecipCountryLib":remove_accents(d["shipping_country_full"]),
                    "Recipemail":remove_accents(d["billing_email"]),
                    "RecipMobileNumber":"",
                    "RecipPhoneNumber":d["shipping_phone"],
                    "DeliveryRelayCountry":"",
                    "DeliveryRelayNumber":""
                },
                "Parcel":{
                    "ShippingServiceKey":"",
                    "ShippingProductCode":"",
                    "InsurranceYN":"",
                    "InsurranceCurrency":"",
                    "ParcelValueCurrency":"",
                    "ParcelWeight":totalwieght,
                    "WeightUnit":"g",
                    "DeliveryInstructions1":prename
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
        totalwieght=0
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
        if 'shipping_country_full' in d:
            del d['shipping_country_full']
        if 'order_total_inc_refund' in d:
            del d['order_total_inc_refund']
        if 'order_total_tax_minus_refund' in d:
            del d['order_total_tax_minus_refund']
        if 'payment_method' in d:
            del d['payment_method']
        modified_data.append(d)
    # Construct response data
    response_data ={
        "Request": 
    {
        "Orders": modified_data
    }}
    # file_name = "response_data.json"

    # with open(file_name, "w") as json_file:
    #     json.dump(response_data, json_file)

    headers = {
        "Token": "KEy5YrFM3EieHYc+CSoFTZlFBtVonvat" 
    } 
    api_url = "https://sl.atomicseller.com/Api/Order/CreateOrders"
    response = requests.post(
        url=api_url,
        json=response_data,
        headers=headers
    )

    if response.status_code == 200:
        print("Response sent successfully.")
    else:
        print("Failed to send response. Status code:", response.status_code)