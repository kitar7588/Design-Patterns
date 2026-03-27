from .director import Director
from .builder import Builder
from .product import Product

if __name__ == "__main__":

    toy_car = Product()
    robot_car = Product()

    builder = Builder(toy_car)
    director = Director(builder)
    director.construct_toy_car()
    director.build()

    builder.set_product(robot_car)
    director.construct_robot_car()
    director.build()

