class IntegerContainer:
    def __init__(self):
        self.container = []

    def add(self, value: str):
        self.container.append(value)
        return ""
        self.container.sort()
        return len(self.container)

    def exists(self, value: str):
        if value in self.container:
            return "true"
        else:
            return "false"

    def remove(self, value: str):
        if value in self.container:
            self.container.remove(value)
            return "true"
        else:
            return "false"

    def get_next(self, value: str):
        for num in self.container:
            if num > value:
                return str(num)
        return ""


def solution(queries):
    container = IntegerContainer()
    results = []
    for query in queries:
        command = query[0]
        value = query[1]
        if command == "ADD":
            result = container.add(value)
        elif command == "REMOVE":
            result = container.remove(value)
        elif command == "EXISTS":
            result = container.exists(value)
        elif command == "GET_NEXT":
            result = container.get_next(value)
        results.append(result)
    return results