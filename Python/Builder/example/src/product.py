from abc import ABC, abstractmethod

class IProduct(ABC):
    @abstractmethod
    def set_label(self, text):
        pass

    @abstractmethod
    def set_material(self, material):
        pass

    @abstractmethod
    def set_packaging(self, packaging):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Product(IProduct):
    _label = None

    def __init__(self):
        pass

    def set_label(self, text):
        self._label = text
        pass

    def set_material(self, material):
        self._material = material
        pass

    def set_packaging(self, packaging):
        self._packaging = packaging
        pass

    def print_info(self):
        if self._label is not None:
            print(f"Label: {self._label}")
        print(f"Material: {self._material}")
        print(f"Packaging: {self._packaging}")
        pass

    def get_info(self):
        return {
            "label": self._label,
            "material": self._material,
            "packaging": self._packaging
        }