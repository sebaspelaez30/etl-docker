from models import Product, Dimensions, Reviews
from typing import List, Dict, Any


def transformed_products(data: Dict[str, Any]) -> List[Product]:
    
    transformed = []

    for raw in data['products']:

        clean_title = raw['title'].strip()
        clean_description = raw['description'].strip()

        clean_price = float(raw["price"])
        clean_rating = float(raw["rating"])
        clean_stock = int(raw["stock"])
        clean_weight = float(raw["weight"])

        clean_brand = raw.get("brand") 

        clean_dimensions = Dimensions(
            width = float(raw["dimensions"]["width"]),
            height = float(raw["dimensions"]["height"]),
            depth = float(raw["dimensions"]["depth"])
        )
                
        clean_reviews = []

        for r in raw['reviews']:
            clean_review = Reviews(
                rating = float(r['rating']),
                comment = r['comment'].strip(),
                date = r['date']
            )
            clean_reviews.append(clean_review)
        
        product = Product(
            id = raw["id"],
            title = clean_title,
            description = clean_description,
            category = raw["category"],
            price = clean_price,
            rating = clean_rating,
            stock = clean_stock,
            tags = raw["tags"],
            weight = clean_weight,
            brand = clean_brand,
            dimensions = clean_dimensions,
            reviews = clean_reviews
        )

        transformed.append(product)

    return transformed

if __name__ == '__main__':
    from fetch import fetch_products
    
    data = fetch_products(limit=5, skip=0)
    clean = transformed_products(data)
    
    print(clean)