class IntegerNumber:
    def __init__(self):
        self.container = []
    def ADD(self, value: int) -> str:
        self.container.append(value)
        return ""
    def REMOVE(self, value: int) -> str:
        if value in self.container:
            self.container.remove(value)
            return "true"
        return "false"
    def EXISTS(self, value: int) -> str:
        if value in self.container:
            return "true"
        return "false"
def solution(queries: list) -> list:
    container = IntegerNumber()
    results = []
    for query in queries:
        command = query[0]
        value = int(query[1])
        if command == "ADD":
            result = container.ADD(value)
        elif command == "REMOVE":
            result = container.REMOVE(value)
        elif command == "EXISTS":
            result = container.EXISTS(value)
        results.append(result)
    return results