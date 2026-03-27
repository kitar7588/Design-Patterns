from abc import ABC, abstractmethod
from .product import IProduct

class IBuilder(ABC):
    @abstractmethod
    def add_label(self, text):
        pass
    @abstractmethod
    def add_material(self):
        pass

    @abstractmethod
    def add_packaging(self):
        pass

    @abstractmethod
    def build(self):
        pass


class Builder(IBuilder):
    _product = None

    def __init__(self,product: IProduct = None):
        self._product = product
        pass

    def set_product(self, product: IProduct):
        self._product = product
        pass

    def add_label(self, text):
        self._product.set_label(text)
        pass

    def add_material(self, material):
        self._product.set_material(material)
        pass

    def add_packaging(self, packaging):
        self._product.set_packaging(packaging)
        pass

    def build(self):
        self._product.print_info()
        return self._product