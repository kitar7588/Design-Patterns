from unittest import TestCase
from example.src import ConcreteFactoryA, ConcreteFactoryB

class TestFactory(TestCase):
    product_ids = [1, 2.5, "B001", "0xff"]

    def test_concrete_factory_a(self):
        print("test ConcreteFactoryA")
        factory_a = ConcreteFactoryA()
        for product_id in self.product_ids:
            product_a = factory_a.create_product(product_id)
            self.assertEqual(product_a.get_id(), product_id)

    def test_concrete_factory_b(self):
        print("test ConcreteFactoryB")
        factory_b = ConcreteFactoryB()
        for product_id in self.product_ids:
            product_b = factory_b.create_product(product_id)
            self.assertEqual(product_b.get_id(), product_id)