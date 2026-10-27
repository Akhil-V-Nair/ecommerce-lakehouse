from dataclasses import dataclass

@dataclass(frozen=True)
class LineItem:
    sku: str
    quantity: int
    unit_price: float

    def line_total(self) -> float:
        return round(self.quantity * self.unit_price, 2)


print(LineItem('SKU-001', 5, 40.0).line_total())