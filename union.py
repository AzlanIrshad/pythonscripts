from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        self.container = []

    def add(self, value: int) -> int:
        self.container.append(value)
        print(f"Added {value} to the container")
        return len(self.container)

    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False

    def get_median(self) -> int | None:
        if not self.container:
            return None
        sorted_container = sorted(self.container)
        n = len(sorted_container)
        mid = n // 2
        if n % 2 == 0:
            return sorted_container[mid - 1]
        else:
            return sorted_container[mid]