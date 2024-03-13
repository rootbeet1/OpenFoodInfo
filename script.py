import openfoodfacts
import json 
import re

def get_product_info(product_name):
    api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")
    data = api.product.text_search(product_name)
   
    with open('test.json', 'w') as f:
        json.dump(data,f,indent=4)
    
    product = data['products'][0]
    
    ecoscore= str(product.get('ecoscore_data').get('grades').get('world'))
    ecoscore=ecoscore.upper()
    print("Eco-score:\n", ecoscore)

    nutriscore=str(product.get('nutrition_grades_tags'))
    nutriscore = " ".join(re.findall("[a-zA-Z]+", nutriscore)).upper()
    print("Nutri-score\n", nutriscore)

    nutriments=str(product.get('nutriments'))
    formatted=nutriments.replace(', ', '\n ')
    formatted=formatted.replace('\'','')
    formatted=formatted.replace('{','')
    formatted=formatted.replace('}','')
    print("Nutriments:\n",formatted)
    
Product=input("Which product are you looking for?\n")
get_product_info(Product)




