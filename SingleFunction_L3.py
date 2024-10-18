class IntegerNumber:
    def __init__(self):
        self.container = []
    def ADD(self, value: int) -> str:
        self.container.append(value)
        self.container.sort()
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
    def GET_NEXT(self, value: int) -> str:
        for num in self.container:
            if num > value:
                return str(num)
        return ""
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
        elif command == "GET_NEXT":
            result = container.GET_NEXT(value)
        results.append(result)
    return results