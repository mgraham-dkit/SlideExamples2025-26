from products import Product


def display_products(products: list[Product]) -> None:
    for product in products:
        print(product)

def calc_profit(product: Product) -> float:
    return product.calc_profit()


products = []
prod1 = Product("Product 1", "Apple TC", 6, 10)
prod2 = Product("Product 2", "Orange BN", 3, 10)
prod3 = Product("Product 3", "Strawberry XM", 10, 11)
products.append(prod1)
products.append(prod2)
products.append(prod3)

print("Product list (in order of entry)")
display_products(products)

print("*" * 20)
products.sort(key=calc_profit)
print("Product list (sorted in ascending order of profit)")
display_products(products)
