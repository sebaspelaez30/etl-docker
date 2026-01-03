from fetch import fetch_products
from transform import transformed_products
from load import load_products
import numpy as np

def main():

    #np.random.seed(22)

    data = fetch_products(200, 0)
    clean_products = transformed_products(data)
    load_products(clean_products)

if __name__ == "__main__":
    main()