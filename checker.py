all_keys = set()
missing = {}

def missing_details(data: dict) -> dict:

    for p in data['products']:
        for key in p.keys():
            all_keys.add(key)

    for key in all_keys:
        missing[key] = sum(1 for p in data["products"] if key not in p)
    
    return missing

if __name__ == '__main__':
    from fetch import fetch_products
    data = fetch_products(100,0)
    print(missing_details(data))