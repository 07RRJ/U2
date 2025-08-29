from collections import Counter
import csv
import os
import locale

def format_currency(value):
    return locale.currency(value, grouping=True)

def load_sales(filename):
    products = {}  #ordbok dictionary
    all_products = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])

            all_products.append(product)
            
            if product in products:
                products[product] += sales
            else:
                products[product] = sales

    return all_products, products

def analyze_sales_data(all_products, products):    

    most_sold_product = Counter(all_products).most_common(1)[0]

    most_lucrative_product = max(products, key=products.get)
    product_value = products[most_lucrative_product]

    print(f"Mest sålda produkt: {most_sold_product[0]}, Antal: {most_sold_product[1]}")
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {format_currency(products.values)}")

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')

all_products, products = load_sales('sales_data.csv')
analyze_sales_data(all_products, products) 