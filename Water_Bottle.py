class WaterBottle:

    def init(self, max_capacity=2):
        self.max_capacity = max_capacity
        self.current_contents = 0

    def fill(self) -> None:
        self.current_contents = self.max_capacity

    def drink(self, amount: float) -> float:
        if amount < 0:
            return 0
        elif self.current_contents <= amount:
            removed_amount = self.current_contents
            self.current_contents = 0
            return removed_amount
        else:
            self.current_contents -= amount
            return amount

    def str(self) -> str:
        return f"The bottle currently holds {self.current_contents:.1f}L of water."
