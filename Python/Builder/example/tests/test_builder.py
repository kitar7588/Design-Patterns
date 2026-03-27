from unittest import TestCase
from example.src import Builder, Product, Director

class TestBuilder(TestCase):

    def test_builder(self):
        product = Product()
        builder = Builder()
        builder.set_product(product)

        director = Director(builder)
        director.construct_toy_car()
        director.build()
        info = product.get_info()

        self.assertEqual(info["label"], "Toy Car", "Product Label didn't match")
        self.assertEqual(info["material"], "Plastic", "Product Material didn't match")
        self.assertEqual(info["packaging"], "Box", "Product Packaging didn't match")
        pass