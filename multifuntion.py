def __init__(self):
    self.container = []


def add(self, value: int):
    self.container.append(value)
    return len(self.container)


def delete(self, value: int):
    if value in self.container:
        self.container.remove(value)
        return True
    else:
        return False


def get_median(self):
    self.container.sort()
    if not self.container:
        return None
    n = len(self.container)
    mid = n // 2
    if n % 2 == 0:
        return self.container[mid - 1]
    else:
        return self.container[mid]