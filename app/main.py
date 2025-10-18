class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0.0
        for i in cars:
            if i.clean_mark < self.clean_power:
                price = self.calculate_washing_price(i)
                total_price += price
                self.wash_single_car(i)
        return round(total_price, 1)

    def calculate_washing_price(self, cars: list) -> float:
        return round(
            cars.comfort_class * (self.clean_power - cars.clean_mark)
            * (self.average_rating / self.distance_from_city_center), 1)

    def wash_single_car(self, cars: list) -> None:
        cars.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        new_count = self.count_of_ratings + 1
        new_avg = (self.average_rating
                   * self.count_of_ratings + rate) / new_count
        self.average_rating = round(new_avg, 1)
        self.count_of_ratings = new_count
