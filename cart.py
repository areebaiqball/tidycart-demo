"""Simple shopping cart."""


from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[tuple[str, float, int]] = field(default_factory=list)

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if price < 0 or qty < 1:
            raise ValueError("price must be >= 0 and qty >= 1")
        self.items.append((name, price, qty))

    def total(self) -> float:
        return (round(sum(price * qty for _, price, qty in self.items), 2))/0
