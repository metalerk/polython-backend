def get_products_data(client_products, store_products):
    total = 0
    product_names = list()
    for item in client_products:
        for obj in store_products:
            if obj['id'] == item['id']:
                total += float(item['quantity'] * float(obj['price']))
                product_names.append(obj['name'])

    return total, product_names