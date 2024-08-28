from math import sqrt
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_list: dict,
        location: list[int, int],
        money: int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_list = product_list
        self.location = location
        self.money = money
        self.car = car

    def distance_to_shop(self, shop: Shop) -> float:
        return sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + ((self.location[1] - shop.location[1]) ** 2)
        )

    def make_purchase(self, shop: Shop) -> float:
        bill = 0
        for product in self.product_list.keys():
            bill += self.product_list[product] * shop.products[product]
        return bill

    def money_to_reach_shop(self, shop: Shop, fuel_price: float) -> float:
        dist = (
            self.distance_to_shop(shop) * fuel_price
            * self.car.volume_consumption / 100
        )
        dist *= 2
        return round(dist, 2)
