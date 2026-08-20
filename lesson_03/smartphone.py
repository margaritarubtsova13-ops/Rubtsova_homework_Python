class Smartphone:
    def __init__(self, brand: str, model: str, phone_number: str) -> None:
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def get_catalog_line(self) -> str:
        return f"{self.brand} - {self.model}. {self.phone_number}"
