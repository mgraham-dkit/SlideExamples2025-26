from __future__ import annotations
from types import NotImplementedType


class Product:
    def __init__(self, prod_id: str, name: str, cost: float, retail: float):
        if prod_id is None:
            print("Product must have a valid product ID")
        self._prod_id = prod_id

        self.name = name
        if not Product.validate_price(cost):
            print("Product cost cannot be less than or equal to 0")
        self.cost = cost

        if not Product.validate_price(retail):
            print("Product retail price cannot be less than or equal to 0")
        self.retail = retail

    def __eq__(self, other: Product) -> NotImplementedType | bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self._prod_id == other._prod_id

    def __ne__(self, other: Product) -> NotImplementedType | bool:
        if not isinstance(other, Product):
            return NotImplemented

        return not self == other

    def __str__(self) -> str:
        return f"{self._prod_id}: {self.name} costs €{self.cost} to manufacture, but sells for €{self.retail}, at a profit of €{self.calc_profit()}"

    def __repr__(self) -> str:
        return f"Product[_prod_id= {self._prod_id}, name={self.name}, cost={self.cost}, retail={self.retail}]"

    def calc_profit(self) -> float:
        return self.retail - self.cost

    @staticmethod
    def validate_price(price):
        if price is None or price <= 0:
            return False

        return True
