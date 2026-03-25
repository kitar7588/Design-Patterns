from example.src import ConcreteFactoryA, ConcreteFactoryB

def create_product(factory,id):
    product = factory.create_product(id)
    return product

if __name__ == "__main__":
    product_a = create_product(ConcreteFactoryA(),"A001")
    product_b = create_product(ConcreteFactoryB(),"B001")

    print(f"Product A ID: {product_a.get_id()}")
    print(f"Product B ID: {product_b.get_id()}")