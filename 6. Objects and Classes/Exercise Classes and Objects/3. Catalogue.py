class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [product for product  in self.products if product[0] == first_letter] # list comprehenshion
       # return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        sorted_products  = sorted(self.products)
        result += "\n".join(sorted_products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
