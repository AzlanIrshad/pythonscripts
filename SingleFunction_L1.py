class IntegerNumber:
    def __init__(self):
        self.container = set()
    def ADD(self, value: int):
        self.container.add(value)
        return ""
    def EXISTS(self, value: int):
        if value in self.container:
            return "true"
        return "false"
def solution(queries):
    container = IntegerNumber()
    results = []
    for query in queries:
        command = query[0]
        value = int(query[1])
        if command == "ADD":
            result = container.ADD(value)
        elif command == "EXISTS":
            result = container.EXISTS(value)
        results.append(result)
    return results