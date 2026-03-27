from .builder import IBuilder

class Director:
    def __init__(self, builder: IBuilder) :
        self._builder = builder

    def construct_toy_car(self) :
        self._builder.add_label("Toy Car")
        self._builder.add_material("Plastic")
        self._builder.add_packaging("Box")
        pass

    def construct_robot_car(self) :
        self._builder.add_material("Metal")
        self._builder.add_packaging("Bag")
        pass

    def build(self):
        return self._builder.build()