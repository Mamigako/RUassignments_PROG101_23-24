class WaterBottle:

    def __init__(self, max_capacity=2):
        self.max_capacity = max_capacity
        self.current_contents = 0

    def __fill__(self) -> None:
        self.current_contents = self.max_capacity

    def __drink__(self, amount: float) -> float:
        if amount < 0:
            return 0
        elif self.current_contents <= amount:
            removed_amount = self.current_contents
            self.current_contents = 0
            return removed_amount
        else:
            self.current_contents -= amount
            return amount

    def __str__(self) -> str:
        return f"The bottle currently holds {self.current_contents:.1f}L of water."